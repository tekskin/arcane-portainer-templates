# Exported Arcane Registry Summary

## Source

- Portainer source registry: https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json
- Conversion target: Arcane-compatible registry export
- Export date: 2026-09-30

## Results

- Source templates found: 201
- Converted successfully: 201
- Failed conversion: 0
- Schema validation: PASS

## Registry output

Generated files are located in the directory below:

- output-technorabilia/
  - registry.json
  - conversion-report.json
  - VALIDATION.md
  - EXPORT_SUMMARY.md
  - templates/

## Compatibility notes

This source is compatible with the existing Portainer-to-Arcane conversion flow. The converter preserved the Portainer template structure, generated Docker Compose files for each template, and produced valid Arcane registry entries with direct file URLs and content hashes.

## Suggested hosting pattern

After publication over HTTPS, the registry can be referenced using a URL in the form:

- https://example.com/arcane-portainer-templates/technorabilia/registry.json

The registry is ready for Arcane import when hosted at a public HTTPS location.

## Validation status

The generated registry was validated against the Arcane registry schema and passed.
