# Sickgear

[SickGear](https://github.com/sickgear/sickgear) provides management of TV shows and/or Anime, it detects new episodes, links downloader apps, and more.. For more information on SickGear visit their website and check it out: https://github.com/SickGear/SickGear

- **Arcane template ID:** `sickgear`
- **Original Portainer name:** `Sickgear`
- **Categories:** Media Management
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/sickgear/configmkdir -p /srv/lsio/sickgear/tvmkdir -p /srv/lsio/sickgear/downloads

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
