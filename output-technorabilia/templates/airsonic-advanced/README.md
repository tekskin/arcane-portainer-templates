# Airsonic-advanced

[Airsonic-advanced](https://github.com/kagemomiji/airsonic-advanced) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

- **Arcane template ID:** `airsonic-advanced`
- **Original Portainer name:** `Airsonic-advanced`
- **Categories:** Media Servers, Music
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/airsonic-advanced/configmkdir -p /srv/lsio/airsonic-advanced/musicmkdir -p /srv/lsio/airsonic-advanced/playlistsmkdir -p /srv/lsio/airsonic-advanced/podcastsmkdir -p /srv/lsio/airsonic-advanced/media

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
