# Lazylibrarian

[Lazylibrarian](https://lazylibrarian.gitlab.io/) is a program to follow authors and grab metadata for all your digital reading needs. It uses a combination of Goodreads Librarything and optionally GoogleBooks as sources for author info and book info. This container is based on the DobyTang fork.

- **Arcane template ID:** `lazylibrarian`
- **Original Portainer name:** `Lazylibrarian`
- **Categories:** Books
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/lazylibrarian/configmkdir -p /srv/lsio/lazylibrarian/downloadsmkdir -p /srv/lsio/lazylibrarian/books

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
