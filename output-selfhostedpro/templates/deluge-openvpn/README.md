# Deluge openvpn

This container contains OpenVPN and Deluge with a configuration where Deluge is running only when OpenVPN has an active tunnel. It bundles configuration files for many popular VPN providers to make the setup easier.

- **Arcane template ID:** `deluge-openvpn`
- **Original Portainer name:** `deluge-openvpn`
- **Categories:** Other, VPN, Tools
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/SelfhostedPro/selfhosted_templates/master/Template/portainer-v2.json

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
