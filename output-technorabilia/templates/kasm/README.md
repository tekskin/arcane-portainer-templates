# Kasm

[Kasm](https://www.kasmweb.com/?utm_campaign=LinuxServer&utm_source=listing) Workspaces is a docker container streaming platform for delivering browser-based access to desktops, applications, and web services. Kasm uses devops-enabled Containerized Desktop Infrastructure (CDI) to create on-demand, disposable, docker containers that are accessible via web browser. Example use-cases include Remote Browser Isolation (RBI), Data Loss Prevention (DLP), Desktop as a Service (DaaS), Secure Remote Access Services (RAS), and Open Source Intelligence (OSINT) collections. The rendering of the graphical-based containers is powered by the open-source project [KasmVNC](https://www.kasmweb.com/kasmvnc.html?utm_campaign=LinuxServer&utm_source=kasmvnc).

- **Arcane template ID:** `kasm`
- **Original Portainer name:** `Kasm`
- **Categories:** Remote Desktop, Business
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/kasm/optmkdir -p /srv/lsio/kasm/profiles

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
