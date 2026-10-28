"""Strict, small scenario schema shared by YAML and JSON."""

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re

import yaml


DEFAULT_SCENARIOS = Path(__file__).parent / "scenarios"
RULE_TYPES = {"required", "forbidden", "ordered", "session_continuity", "no_repeated_greeting"}


class ScenarioError(ValueError):
    pass


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently losing an assertion."""


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if not isinstance(key, str) or key in result:
            raise ScenarioError("Scenario keys must be unique strings.")
        result[key] = value
    return result


def _yaml_mapping(loader, node):
    return _unique_pairs(
        (loader.construct_object(key, deep=True), loader.construct_object(value, deep=True))
        for key, value in node.value
    )


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _yaml_mapping)


def _mapping(value, allowed: set[str], required: set[str], where: str):
    if not isinstance(value, dict) or not required <= value.keys() or value.keys() - allowed:
        raise ScenarioError(f"{where}: missing required fields or unknown fields; see scenario schema.")


def _string(value, where: str):
    if not isinstance(value, str) or not value.strip():
        raise ScenarioError(f"{where}: expected a nonempty string.")


@dataclass(frozen=True)
class Scenario:
    definition: dict
    sha256: str

    @property
    def id(self) -> str:
        return self.definition["id"]

    @property
    def version(self) -> str:
        return self.definition["version"]

    @property
    def product(self) -> str:
        return self.definition["product"]

    @property
    def turns(self) -> list[dict]:
        return self.definition["turns"]

    @property
    def concepts(self) -> dict[str, list[str]]:
        return self.definition["concepts"]

    def rules_for(self, turn: dict) -> list[dict]:
        return self.definition.get("assertions", []) + turn["assertions"]


def parse_scenario(data: object) -> Scenario:
    required = {"schema_version", "id", "version", "product", "concepts", "turns"}
    _mapping(data, required | {"description", "country", "assertions"}, required, "scenario")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ScenarioError("scenario.schema_version must be 1.")
    for key in ("id", "version", "product", "description", "country"):
        if key in data:
            _string(data[key], f"scenario.{key}")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,99}", data["id"]):
        raise ScenarioError("Scenario ID must use 1-100 letters, digits, underscores or hyphens.")
    concepts = data["concepts"]
    if not isinstance(concepts, dict) or not concepts:
        raise ScenarioError("scenario.concepts must be a nonempty mapping.")
    for name, patterns in concepts.items():
        _string(name, "concept name")
        if not isinstance(patterns, list) or not patterns:
            raise ScenarioError("Each concept needs a nonempty list of regex alternatives.")
        for pattern in patterns:
            _string(pattern, f"concept {name}")
            try:
                if re.compile(pattern, re.I | re.M).search(""):
                    raise ScenarioError(f"Concept {name} must not match empty text.")
            except re.error:
                raise ScenarioError(f"Concept {name} has an invalid regular expression.") from None

    def references(names, where):
        if not isinstance(names, list) or not names:
            raise ScenarioError(f"{where}: expected a nonempty list of concept names.")
        if any(not isinstance(name, str) or name not in concepts for name in names):
            raise ScenarioError(f"{where}: unknown concept reference.")

    def rules(items, where):
        if not isinstance(items, list):
            raise ScenarioError(f"{where}: assertions must be a list.")
        ids = set()
        for rule in items:
            base = {"id", "type", "severity", "reason", "products"}
            specific = {
                "required": {"concepts"},
                "forbidden": {"concepts", "unless_merchant_concepts", "unless_response_concepts"},
                "ordered": {"steps"},
                "session_continuity": set(),
                "no_repeated_greeting": {"concepts"},
            }
            if (
                not isinstance(rule, dict) or not isinstance(rule.get("type"), str)
                or rule["type"] not in RULE_TYPES
            ):
                raise ScenarioError(f"{where}: unknown assertion type.")
            _mapping(rule, base | specific[rule["type"]], {"id", "type", "reason"}, where)
            for key in ("id", "reason"):
                _string(rule[key], where)
            if rule["id"] in ids or rule["id"].startswith("transport."):
                raise ScenarioError(f"{where}: duplicate or reserved assertion ID.")
            ids.add(rule["id"])
            if rule.get("severity", "fail") not in ("fail", "warning"):
                raise ScenarioError(f"{where}: severity must be fail or warning.")
            if "products" in rule:
                if not isinstance(rule["products"], list) or not rule["products"]:
                    raise ScenarioError(f"{where}: products must be a nonempty list.")
                for product in rule["products"]:
                    _string(product, where)
            kind = rule["type"]
            if kind in {"required", "forbidden", "no_repeated_greeting"}:
                references(rule.get("concepts"), where)
            if kind == "ordered":
                if not isinstance(rule.get("steps"), list) or len(rule["steps"]) < 2:
                    raise ScenarioError(f"{where}: ordered needs at least two steps.")
                for step in rule["steps"]:
                    references([step] if isinstance(step, str) else step, where)
            for condition in ("unless_merchant_concepts", "unless_response_concepts"):
                if condition in rule:
                    references(rule[condition], where)
        return ids

    common_ids = rules(data.get("assertions", []), "scenario.assertions")
    if not isinstance(data["turns"], list) or not data["turns"]:
        raise ScenarioError("Scenario needs at least one turn.")
    turn_ids = set()
    for index, turn in enumerate(data["turns"], 1):
        where = f"turn {index}"
        _mapping(turn, {"id", "merchant", "assertions"}, {"id", "merchant", "assertions"}, where)
        _string(turn["id"], where)
        _string(turn["merchant"], where)
        if turn["id"] in turn_ids:
            raise ScenarioError(f"{where}: duplicate turn ID.")
        turn_ids.add(turn["id"])
        if common_ids & rules(turn["assertions"], where):
            raise ScenarioError(f"{where}: assertion ID also appears in common assertions.")
        applicable = data.get("assertions", []) + turn["assertions"]
        if not any(
            rule["type"] in {"required", "forbidden", "ordered"}
            and rule.get("severity", "fail") == "fail"
            and data["product"] in rule.get("products", [data["product"]])
            for rule in applicable
        ):
            raise ScenarioError(f"{where}: needs an applicable hard behavioral assertion.")
    canonical = json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return Scenario(data, hashlib.sha256(canonical).hexdigest())


def load_scenario(path: Path) -> Scenario:
    try:
        text = path.read_text(encoding="utf-8-sig")
        if path.suffix.lower() == ".json":
            data = json.loads(text, object_pairs_hook=_unique_pairs)
        else:
            data = yaml.load(text, Loader=UniqueLoader)
        return parse_scenario(data)
    except (OSError, UnicodeError, yaml.YAMLError, json.JSONDecodeError, RecursionError):
        # Parser exceptions can include source lines with accidentally pasted secrets.
        raise ScenarioError("Cannot read scenario: invalid YAML/JSON, encoding, or file path.") from None


def load_catalog(directory: Path = DEFAULT_SCENARIOS) -> dict[str, Scenario]:
    paths = sorted(path for path in directory.glob("*") if path.suffix.lower() in {".yaml", ".yml", ".json"})
    if not paths:
        raise ScenarioError("No YAML or JSON scenario files found.")
    catalog = {}
    for path in paths:
        scenario = load_scenario(path)
        if scenario.id in catalog:
            raise ScenarioError("Duplicate scenario ID in scenario directory.")
        catalog[scenario.id] = scenario
    return catalog
