# Exported Arcane Registry Summary

## Source

- Portainer source registry: https://raw.githubusercontent.com/SelfhostedPro/selfhosted_templates/master/Template/portainer-v2.json
- Conversion target: Arcane-compatible registry export
- Export date: 2026-09-30

## Results

- Source templates found: 106
- Converted successfully: 105
- Failed conversion: 1
- Schema validation: PASS

## Excluded item

One upstream template entry was excluded because the source repository contains a broken stackfile reference for `pritunl`:

- `Template/Stack/pritunl.yml` -> GitHub raw URL returned HTTP 404

This is not a schema problem or Arcane compatibility issue. It is a source-data issue in the upstream Portainer registry, and the converter reports it in `conversion-report.json` instead of producing a broken Arcane entry.

## Registry output

Generated files are located in the directory below:

- output-selfhostedpro/
  - registry.json
  - conversion-report.json
  - VALIDATION.md
  - EXPORT_SUMMARY.md
  - templates/

## Compatibility notes

The SelfhostedPro source is generally compatible with the existing Portainer-to-Arcane conversion flow. The converter successfully handled null metadata cases and invalid optional description values, and the resulting Arcane registry validates against the live schema.

## Suggested hosting pattern

After publication over HTTPS, the registry can be referenced using a URL in the form:

- https://example.com/arcane-portainer-templates/selfhostedpro/registry.json

The registry is ready for Arcane import once hosted at a public HTTPS location.

## Validation status

The generated registry was validated against the Arcane registry schema and passed.
