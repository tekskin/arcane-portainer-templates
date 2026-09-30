# Calibre-web

[Calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database. It is also possible to integrate google drive and edit metadata and your calibre library through the app itself. This software is a fork of library and licensed under the GPL v3 License.

- **Arcane template ID:** `calibre-web`
- **Original Portainer name:** `Calibre-web`
- **Categories:** Books
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/calibre-web/configmkdir -p /srv/lsio/calibre-web/books

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
