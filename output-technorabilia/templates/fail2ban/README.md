# Fail2ban

[Fail2ban](http://www.fail2ban.org/) is a daemon to ban hosts that cause multiple authentication errors.

- **Arcane template ID:** `fail2ban`
- **Original Portainer name:** `Fail2ban`
- **Categories:** Network, Security
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/technorabilia/portainer-templates/main/lsio/templates/templates.json

## Original Portainer notes

Portainer App Templates by Technorabilia, based on data provided by LinuxServer.io.Ensure to create the following volume directories on the host file system, or modify the paths in the volume mapping section under the advanced options below, as needed.mkdir -p /srv/lsio/fail2ban/configmkdir -p /srv/lsio/fail2ban/var/log:romkdir -p /srv/lsio/fail2ban/remotelogs/airsonic:romkdir -p /srv/lsio/fail2ban/remotelogs/apache2:romkdir -p /srv/lsio/fail2ban/remotelogs/authelia:romkdir -p /srv/lsio/fail2ban/remotelogs/emby:romkdir -p /srv/lsio/fail2ban/remotelogs/filebrowser:romkdir -p /srv/lsio/fail2ban/remotelogs/homeassistant:romkdir -p /srv/lsio/fail2ban/remotelogs/lighttpd:romkdir -p /srv/lsio/fail2ban/remotelogs/nextcloud:romkdir -p /srv/lsio/fail2ban/remotelogs/nginx:romkdir -p /srv/lsio/fail2ban/remotelogs/nzbget:romkdir -p /srv/lsio/fail2ban/remotelogs/overseerr:romkdir -p /srv/lsio/fail2ban/remotelogs/prowlarr:romkdir -p /srv/lsio/fail2ban/remotelogs/radarr:romkdir -p /srv/lsio/fail2ban/remotelogs/sabnzbd:romkdir -p /srv/lsio/fail2ban/remotelogs/sonarr:romkdir -p /srv/lsio/fail2ban/remotelogs/unificontroller:romkdir -p /srv/lsio/fail2ban/remotelogs/vaultwarden:ro

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
