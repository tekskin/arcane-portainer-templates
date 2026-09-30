#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import urllib.request

SCHEMA_URLS = [
    "https://registry.getarcane.app/schema.json",
    "https://raw.githubusercontent.com/getarcaneapp/arcane-templates/main/schema.json",
]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "arcane-registry-validator/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    registry_path = Path(sys.argv[1] if len(sys.argv) > 1 else "output/registry.json")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))

    try:
        import jsonschema
    except ImportError:
        print("jsonschema is not installed. Structural JSON validation only.")
        print("Install with: python -m pip install jsonschema")
        return 0

    last = None
    for url in SCHEMA_URLS:
        try:
            schema = fetch(url)
            jsonschema.Draft7Validator.check_schema(schema)
            jsonschema.Draft7Validator(schema).validate(registry)
            print(f"PASS: {registry_path} validates against {url}")
            return 0
        except Exception as exc:
            last = exc
    print("FAIL: could not validate against the Arcane Draft-07 schema.")
    print(last)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
