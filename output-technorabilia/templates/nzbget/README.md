# Nzbget

[Nzbget](http://nzbget.com/) is a usenet downloader, written in C++ and designed with performance in mind to achieve maximum download speed by using very little system resources.

- **Arcane template ID:** `nzbget`
- **Original Portainer name:** `Nzbget`
- **Categories:** Downloaders
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/nzbget/configmkdir -p /srv/lsio/nzbget/downloads

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
