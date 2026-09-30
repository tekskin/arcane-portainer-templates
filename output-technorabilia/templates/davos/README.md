# Davos

davos is an FTP automation tool that periodically scans given host locations for new files. It can be configured for various purposes, including listening for specific files to appear in the host location, ready for it to download and then move, if required. It also supports completion notifications as well as downstream API calls, to further the workflow.

- **Arcane template ID:** `davos`
- **Original Portainer name:** `davos`
- **Categories:** FTP, Other, Tools
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

## Original Portainer notes

Configuration /config - AppData Location
/downloads - File Download Location

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
