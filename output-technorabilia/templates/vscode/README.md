# Vscode

[VS Code](https://code.visualstudio.com/) is an integrated development environment developed by Microsoft. This container runs the full desktop application, for a web native version see [Code Server](https://github.com/linuxserver/docker-code-server).

- **Arcane template ID:** `vscode`
- **Original Portainer name:** `Vscode`
- **Categories:** Programming
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/vscode/config

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
