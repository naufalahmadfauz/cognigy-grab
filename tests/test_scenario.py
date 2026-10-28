from copy import deepcopy
import json

import pytest

from uc4_runner.scenario import ScenarioError, load_catalog, load_scenario, parse_scenario


def test_yaml_and_json_have_same_semantic_hash(tmp_path, scenario):
    path = tmp_path / "scenario.json"
    path.write_text(json.dumps(scenario.definition), encoding="utf-8")
    assert load_scenario(path).sha256 == scenario.sha256


@pytest.mark.parametrize("change", [
    lambda data: data.update(schema_version=2),
    lambda data: data.update(schema_version=True),
    lambda data: data.update(extra_field="typo"),
    lambda data: data.update(id="../bad-path"),
    lambda data: data.update(turns=[]),
    lambda data: data["concepts"].update(grabmart=["["]),
    lambda data: data["concepts"].update(grabmart=[".*"]),
    lambda data: data["turns"][0].update(merchant=""),
    lambda data: data["turns"][0]["assertions"][0].update(concepts=["unknown"]),
    lambda data: data["turns"][0]["assertions"][0].update(type="unknown"),
    lambda data: data["turns"][0]["assertions"][0].update(type=[]),
    lambda data: data["turns"][0]["assertions"][0].update(severity=[]),
    lambda data: data["turns"][0]["assertions"][0].update(id="identity-continuity"),
    lambda data: data["turns"][0].update(assertions=[]),
    lambda data: data["turns"][1]["assertions"][0].update(steps=["portal"]),
    lambda data: data["turns"][1]["assertions"][0].update(steps=["portal", ["unknown"]]),
    lambda data: data.update(concept_exclusions=[]),
    lambda data: data.update(concept_exclusions={"unknown": ["word"]}),
    lambda data: data.update(concept_exclusions={"grabmart": ["["]}),
    lambda data: data.update(concept_exclusions={"grabmart": [".*"]}),
    lambda data: data["turns"][0]["assertions"][0].update(allow_merchant_context=["unknown"]),
    lambda data: data["turns"][0]["assertions"][0].update(allow_merchant_context=["portal"]),
    lambda data: data["turns"][0]["assertions"][1].update(allow_merchant_context=["grabmart"]),
    lambda data: data["turns"][1]["assertions"][-1].update(warn_if_response_concepts=["unknown"]),
    lambda data: data["turns"][1]["assertions"][-1].update(severity="warning"),
])
def test_invalid_scenarios_fail_before_execution(scenario, change):
    data = deepcopy(scenario.definition)
    change(data)
    with pytest.raises(ScenarioError):
        parse_scenario(data)


@pytest.mark.parametrize("suffix,content", [
    ("yaml", "id: one\nid: two\n"), ("json", '{"id":"one","id":"two"}'),
    ("yaml", "!!python/object/apply:os.system ['echo unsafe']"), ("json", "{bad"),
    ("yaml", "[unclosed"),
])
def test_invalid_files_are_rejected_safely(tmp_path, suffix, content):
    path = tmp_path / f"bad.{suffix}"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ScenarioError):
        load_scenario(path)


def test_duplicate_scenario_ids_are_rejected(tmp_path, scenario):
    for name in ("one.json", "two.json"):
        (tmp_path / name).write_text(json.dumps(scenario.definition), encoding="utf-8")
    with pytest.raises(ScenarioError, match="Duplicate scenario ID"):
        load_catalog(tmp_path)
