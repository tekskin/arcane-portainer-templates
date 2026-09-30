# Mame

[MAME](https://www.mamedev.org/) is a free and open-source emulator designed to emulate the hardware of arcade games, video game consoles, old computers and other systems in software on modern personal computers.

- **Arcane template ID:** `mame`
- **Original Portainer name:** `Mame`
- **Categories:** Games
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/mame/configmkdir -p /srv/lsio/mame/mame:ro

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
