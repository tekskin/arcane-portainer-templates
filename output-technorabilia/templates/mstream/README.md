# Mstream

[Mstream](https://mstream.io/) is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere. There are mobile apps available for both Android and iPhone.

- **Arcane template ID:** `mstream`
- **Original Portainer name:** `Mstream`
- **Categories:** Media Servers, Music
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/mstream/configmkdir -p /srv/lsio/mstream/music

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
