# Ubooquity

[Ubooquity](https://vaemendis.net/ubooquity/) is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer.

- **Arcane template ID:** `ubooquity`
- **Original Portainer name:** `Ubooquity`
- **Categories:** Books
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/ubooquity/configmkdir -p /srv/lsio/ubooquity/booksmkdir -p /srv/lsio/ubooquity/comicsmkdir -p /srv/lsio/ubooquity/files

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
