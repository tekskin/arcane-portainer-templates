# Let's Encrypt / SWAG

This container sets up an Nginx webserver and reverse proxy with php support and a built-in letsencrypt client that automates free SSL server certificate generation and renewal processes. It also contains fail2ban for intrusion prevention.

- **Arcane template ID:** `letsencrypt-swag`
- **Original Portainer name:** `letsencrypt / SWAG`
- **Categories:** Tools, Web
- **Source type:** Portainer `1`
- **Original source:** https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

## Original Portainer notes

Before running this container, make sure that the url and subdomains are properly forwarded to this container's host.- Port 443 on the internet side of the router should be forwarded to this container's port 443.
- If you need a dynamic dns provider, you can use the free provider duckdns.org where the url will be yoursubdomain.duckdns.org and the subdomains can be www,ftp,cloud
- The container detects changes to url and subdomains, revokes existing certs and generates new ones during start.
- It also detects changes to the DHLEVEL parameter and replaces the dhparams file.
- If you'd like to password protect your sites, you can use htpasswd. Run the following command on your host to generate the htpasswd file docker exec -it letsencrypt htpasswd -c /config/nginx/.htpasswd <username>

## Conversion notes

This template was generated from the Portainer community template registry.
Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.
Container-only mounts remain anonymous Docker volumes.
Review ports, permissions, image tags, environment variables, and persistent
storage before deploying.
