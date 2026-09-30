# Watchtower

With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your own image registry. Watchtower will pull down your new image, gracefully shut down your existing container and restart it with the same options that were used when it was deployed initially.

- **Arcane template ID:** `watchtower`
- **Original Portainer name:** `watchtower`
- **Categories:** Other, Tools, Maintenance
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/SelfhostedPro/selfhosted_templates/master/Template/portainer-v2.json

## Original Portainer notes

It is recommended to manually update your containers but we're including this for those of you that don't care

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
