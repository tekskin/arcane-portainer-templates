# Portainer → Arcane complete registry conversion

This package builds a complete Arcane Templates Registry from the exact
Portainer source:

https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

The source currently contains **112 templates**:
- **107** Portainer `type: 1` single-container templates
- **5** Portainer `type: 3` stack templates

## Why this is generated instead of shipping a fake `registry.json`

Arcane requires every registry template to expose direct HTTPS URLs for the
Compose file and optional environment/documentation files. The original
Portainer registry embeds single-container definitions directly in
`template.json`, so there is no existing Compose URL for those 107 entries.

The converter therefore creates the missing Compose files and then produces a
valid Arcane registry pointing at your own hosting location.

The five Portainer stack templates are retrieved from their referenced stack
files instead of being re-created from memory.

## Build

Python 3.10+ is recommended.

### Local filesystem

```powershell
python .\build_arcane_registry.py --base-url https://YOUR-HOST/arcane-portainer-templates
```

This creates:

```text
output/
  registry.json
  conversion-report.json
  VALIDATION.md
  templates/
    <template-id>/
      compose.yaml
      .env.example
      README.md
```

### GitHub Pages / raw GitHub

For a repository:

```text
https://github.com/YOURUSER/arcane-portainer-templates
```

with the generated `output` contents copied to the repository root, use:

```powershell
python .\build_arcane_registry.py --base-url https://raw.githubusercontent.com/YOURUSER/arcane-portainer-templates/main
```

Then the Arcane registry URL is:

```text
https://raw.githubusercontent.com/YOURUSER/arcane-portainer-templates/main/registry.json
```

## Important conversion behaviour

### `/portainer` paths

Original Portainer paths such as:

```text
/portainer/Files/AppData/Config/Bazarr
```

become:

```text
${PORTAINER_ROOT}/Files/AppData/Config/Bazarr
```

and `.env.example` contains:

```text
PORTAINER_ROOT=/mnt/portainer
```

Change that value to the directory appropriate for the Docker host.

### Anonymous volumes

A Portainer mount with a container path but no host bind is retained as an
anonymous Docker volume.

### Environment variables

Portainer `default` and `set` values are converted into Compose environment
variables and documented in `.env.example`.

### Port mappings

Container-only Portainer mappings such as `80/tcp` are retained as
container-only Compose mappings rather than inventing a host port.

### Notes and documentation

The original Portainer `description`, `categories`, and `note` information is
retained in each template's README where possible.

## Validation

Install the optional JSON Schema validator:

```powershell
python -m pip install jsonschema
python .\validate_arcane_registry.py
```

The validator retrieves Arcane's current Draft-07 schema and validates the
generated `registry.json`.

## Arcane import

After hosting the generated directory over HTTPS, add the raw URL of:

```text
registry.json
```

in Arcane's Templates / Custom Registries configuration.

Arcane's documentation specifies that registry files use the Arcane Templates
Registry Schema (Draft 07), and that Compose/environment URLs must point to
directly accessible files rather than repository HTML pages.

## Source fidelity

This conversion intentionally does not claim that old Portainer images are
current or secure. It preserves the source registry's image references and
configuration so that the conversion is faithful to the requested source.

Before deploying an individual template, review:
- image availability and age
- image tags
- host paths
- permissions
- exposed ports
- required secrets
- privileged/device requirements
- application-specific configuration

See `conversion-report.json` for the exact conversion result.
