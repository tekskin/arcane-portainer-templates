# Medusa

[Medusa](https://pymedusa.com/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

- **Arcane template ID:** `medusa`
- **Original Portainer name:** `Medusa`
- **Categories:** Media Management
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/medusa/configmkdir -p /srv/lsio/medusa/downloadsmkdir -p /srv/lsio/medusa/tv

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
