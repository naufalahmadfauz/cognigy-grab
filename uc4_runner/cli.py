"""Small argparse CLI; dry-run and validation never construct an HTTP client."""

import argparse
from dataclasses import replace
from pathlib import Path
import sys

from . import __version__
from .config import Config, ConfigError
from .redact import Redactor
from .runner import execute_batch
from .scenario import DEFAULT_SCENARIOS, ScenarioError, load_catalog, load_scenario


def _positive(value: str) -> int:
    try:
        result = int(value)
        if result > 0:
            return result
    except ValueError:
        pass
    raise argparse.ArgumentTypeError("must be a positive integer")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="UC4 Cognigy conversation test runner")
    root.add_argument("--version", action="version", version=__version__)
    commands = root.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="Validate scenarios and environment without network access")
    run = commands.add_parser("run", help="Run an isolated conversation batch or make an offline plan")
    for command in (validate, run):
        source = command.add_mutually_exclusive_group()
        source.add_argument("--scenario-file", type=Path, help="One YAML or JSON scenario")
        source.add_argument("--scenarios-dir", type=Path, default=DEFAULT_SCENARIOS, help="Directory of scenario files")
    run.add_argument("--scenario", help="Scenario ID (required unless --scenario-file is supplied)")
    run.add_argument("--repeat", type=_positive, default=5)
    run.add_argument("--dry-run", action="store_true", help="Write planned conversations; make no HTTP requests")
    run.add_argument("--output-dir", type=Path, default=Path("reports"))
    run.add_argument("--concurrency", type=int, choices=range(1, 9), help="Maximum independent sessions in flight")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    config = None
    try:
        config = Config.from_env(require_endpoint=args.command == "run" and not args.dry_run)
        if args.scenario_file:
            scenario = load_scenario(args.scenario_file)
            catalog = {scenario.id: scenario}
        else:
            catalog = load_catalog(args.scenarios_dir)
        if args.command == "validate":
            print(f"Validated {len(catalog)} scenario(s); environment valid. No requests sent.")
            return 0
        scenario_id = args.scenario or (next(iter(catalog)) if args.scenario_file else None)
        if scenario_id not in catalog:
            raise ScenarioError("Select a known --scenario ID or provide --scenario-file.")
        if args.concurrency is not None:
            config = replace(config, concurrency=args.concurrency)
        if config.retain_raw and not args.dry_run:
            print("Raw evidence retention enabled: redacted responses may still contain sensitive data.", file=sys.stderr)
        directory, batch = execute_batch(
            catalog[scenario_id], config, args.output_dir, repeat=args.repeat, dry_run=args.dry_run,
        )
        # Only aggregate counters and a generated directory name enter console logs.
        print(f"Batch: {directory.name} (inside the selected output directory)")
        if args.dry_run:
            print(f"DRY_RUN: {args.repeat} planned runs; no requests sent; behavior not evaluated.")
            return 0
        counts = batch["metrics"]["outcomes"]
        print("; ".join(f"{name}={count}" for name, count in counts.items()))
        return 2 if counts["ERROR"] else 1 if counts["FAIL"] else 0
    except (ConfigError, ScenarioError) as error:
        message = Redactor(config).text(str(error)) if config else str(error)
        print(f"Error: {message}", file=sys.stderr)
        return 2
    except OSError:
        # File errors can expose caller-supplied paths; keep console output generic.
        print("Error: cannot read/write local files. Check paths, permissions, and available disk space.", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted. Completed run files remain; inspect the batch manifest before using results.", file=sys.stderr)
        return 130
