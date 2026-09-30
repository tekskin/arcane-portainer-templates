# Diskover

[Diskover](https://github.com/diskoverdata/diskover-community) is an open source file system indexer that uses Elasticsearch to index and manage data across heterogeneous storage systems.

- **Arcane template ID:** `diskover`
- **Original Portainer name:** `Diskover`
- **Categories:** Storage, Monitoring
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/diskover/configmkdir -p /srv/lsio/diskover/data

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
