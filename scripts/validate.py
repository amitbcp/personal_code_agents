"""Validate native agent configuration and retained Python syntax without execution."""
import ast
import json
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def main():
    agents = list((ROOT / "agents").glob("*.toml"))
    names = set()
    for path in agents:
        agent = tomllib.loads(path.read_text())
        for key in ("name", "description", "developer_instructions", "model", "model_reasoning_effort"):
            assert isinstance(agent.get(key), str) and agent[key].strip(), (path, key)
        assert agent["name"] not in names, path
        names.add(agent["name"])
        assert agent["sandbox_mode"] in {"read-only", "workspace-write"}, path
    scripts = list((ROOT / "skills").rglob("*.py"))
    for path in scripts:
        ast.parse(path.read_text(), filename=str(path))
    provenance = json.loads((ROOT / "provenance.json").read_text())
    for item in provenance["imports"]:
        assert (ROOT / item["destination"]).exists(), item
        assert (ROOT / item["license_file"]).is_file(), item
    print(f"Valid: {len(agents)} agents, {len(scripts)} Python files, {len(provenance['imports'])} import mappings")


if __name__ == "__main__":
    main()
