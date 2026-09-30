# Pelorus

[Pelorus](https://github.com/linuxserver/pelorus) is an AI navigator for Selkies-powered Linux desktops. Pelorus runs a FastAPI server that gives an LLM agent (Ollama, OpenAI-compatible, or Gemini) control over mouse, keyboard, screenshot, and window management via the [Pixelflux computer-use backend](https://github.com/linuxserver/pixelflux#computer-use-interface-wayland), a Linux accessibility tree (AT-SPI), and optional KWin D-Bus integration.

- **Arcane template ID:** `pelorus`
- **Original Portainer name:** `Pelorus`
- **Categories:** Remote Desktop, AI
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/pelorus/config

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
