# Duck DNS

Duck DNS is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice. The service is completely free, and doesn't require reactivation or forum posts to maintain its existence.

- **Arcane template ID:** `duckdns`
- **Original Portainer name:** `duckdns`
- **Categories:** DNS, Tools
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

## Original Portainer notes

ConfigurationFirst, go to duckdns site, register your subdomain and retrieve your tokenThen run the docker create command above with your subdomain(s) and tokenIt will update your IP with the DuckDNS service every 5 minutes

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
