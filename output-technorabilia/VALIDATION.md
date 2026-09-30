# Validation

- Source templates found: **112**
- Converted successfully: **112**
- Failed conversion: **0**
- Registry structural validation: **PASS**

The generated registry contains only fields documented by Arcane's registry schema.
If `jsonschema` is installed, validate against the live Draft-07 schema with:

```bash
python -m pip install jsonschema
python validate_arcane_registry.py
```

The registry and every referenced file must be hosted at publicly accessible HTTPS URLs.
Raw GitHub URLs are suitable.
