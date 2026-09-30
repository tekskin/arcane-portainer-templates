# Deluge

[Deluge](http://deluge-torrent.org/) is a lightweight, Free Software, cross-platform BitTorrent client. * Full Encryption * WebUI * Plugin System * Much more...

- **Arcane template ID:** `deluge`
- **Original Portainer name:** `Deluge`
- **Categories:** Downloaders
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/deluge/configmkdir -p /srv/lsio/deluge/downloads

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
