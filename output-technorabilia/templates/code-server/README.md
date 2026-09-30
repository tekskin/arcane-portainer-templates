# Code-server

[Code-server](https://coder.com) is VS Code running on a remote server, accessible through the browser. - Code on your Chromebook, tablet, and laptop with a consistent dev environment. - If you have a Windows or Mac workstation, more easily develop for Linux. - Take advantage of large cloud servers to speed up tests, compilations, downloads, and more. - Preserve battery life when you're on the go. - All intensive computation runs on your server. - You're no longer running excess instances of Chrome.

- **Arcane template ID:** `code-server`
- **Original Portainer name:** `Code-server`
- **Categories:** Programming
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/code-server/config

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
