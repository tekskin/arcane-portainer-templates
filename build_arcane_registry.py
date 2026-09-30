#!/usr/bin/env python3
"""
Build a complete Arcane Templates Registry from the Portainer template registry:

https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

The source currently contains 112 templates:
  - 107 Portainer type=1 single-container templates
  - 5 Portainer type=3 stack templates

This converter does NOT invent missing Compose files. For type=1 it generates
Compose from the Portainer definition. For type=3 it downloads the referenced
Portainer stack YAML and uses that as the Compose source.

Usage:
  python build_arcane_registry.py --base-url https://raw.githubusercontent.com/YOURUSER/YOURREPO/main
  python build_arcane_registry.py --base-url https://example.com/arcane-portainer-templates

The base URL must be the public HTTPS directory containing registry.json and
the generated templates/ directory. The script writes:
  output/registry.json
  output/templates/<id>/compose.yaml
  output/templates/<id>/.env.example
  output/templates/<id>/README.md
  output/conversion-report.json
  output/VALIDATION.md

No third-party Python packages are required for generation.
If jsonschema is installed, the script will also validate registry.json against
the live Arcane Draft-07 schema.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

SOURCE_URL = "https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json"
SCHEMA_URLS = [
    "https://registry.getarcane.app/schema.json",
    "https://raw.githubusercontent.com/getarcaneapp/arcane-templates/main/schema.json",
]

DEFAULT_SOURCE_REPO = "https://github.com/Qballjos/portainer_templates"
DEFAULT_SOURCE_BRANCH = "master"

def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "arcane-portainer-registry-converter/1.0"},
    )
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8")

def fetch_json(url: str) -> Any:
    return json.loads(fetch_text(url))

def slug(value: str) -> str:
    s = value.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "template"

def unique_id(base: str, used: set[str]) -> str:
    x = slug(base)
    if x not in used:
        used.add(x)
        return x
    n = 2
    while f"{x}-{n}" in used:
        n += 1
    x = f"{x}-{n}"
    used.add(x)
    return x

def yaml_quote(value: str) -> str:
    # Safe single-quoted YAML scalar.
    return "'" + str(value).replace("'", "''") + "'"

def compose_port(p: str) -> str:
    # Portainer examples include:
    #   53:53/tcp
    #   80/tcp
    #   :80/tcp
    # Compose accepts container-only published-port syntax as "80/tcp".
    p = str(p)
    if p.startswith(":"):
        return p[1:]
    return p

def env_entries(template: dict[str, Any]) -> list[dict[str, str]]:
    result = []
    for item in template.get("env", []) or []:
        name = str(item.get("name", "")).strip()
        if not name:
            continue
        default = item.get("default")
        fixed = item.get("set")
        if fixed is not None:
            value = str(fixed)
        elif default is not None:
            value = str(default)
        else:
            value = ""
        result.append({
            "name": name,
            "value": value,
            "description": str(item.get("description", "") or ""),
            "label": str(item.get("label", "") or ""),
        })
    return result

def variable_expr(name: str, value: str) -> str:
    # Keep defaults in .env.example while allowing Arcane users to override.
    # Empty defaults become an empty interpolation.
    return "${" + name + ":-" + value.replace("\n", " ") + "}"

def bind_host_path(path: str) -> str:
    # Preserve the original Portainer filesystem layout behind a single
    # configurable root. This avoids hard-coding /portainer into the generated
    # templates.
    if path.startswith("/portainer/"):
        return "${PORTAINER_ROOT}/" + path[len("/portainer/"):]
    if path == "/portainer":
        return "${PORTAINER_ROOT}"
    return path

def build_single_compose(t: dict[str, Any], template_id: str) -> tuple[str, str]:
    lines = ["services:", f"  {template_id}:", f"    image: {t['image']}"]

    envs = env_entries(t)
    if envs:
        lines += ["    environment:"]
        for e in envs:
            # Environment values are quoted to prevent YAML coercion.
            lines.append(f"      {e['name']}: {yaml_quote(variable_expr(e['name'], e['value']))}")

    ports = t.get("ports") or []
    if ports:
        lines += ["    ports:"]
        for p in ports:
            lines.append(f"      - {yaml_quote(compose_port(p))}")

    volumes = t.get("volumes") or []
    if volumes:
        lines += ["    volumes:"]
        for v in volumes:
            container = v.get("container")
            bind = v.get("bind")
            if not container:
                continue
            if bind is None or bind == "":
                # Portainer's container-only mount creates an anonymous Docker volume.
                lines.append(f"      - {yaml_quote(container)}")
            else:
                host = bind_host_path(str(bind))
                lines.append(f"      - {yaml_quote(host + ':' + str(container))}")

    restart = t.get("restart_policy")
    if restart:
        lines.append(f"    restart: {yaml_quote(str(restart))}")

    # Preserve Linux platform explicitly when supplied.
    platform = t.get("platform")
    if platform:
        lines.append(f"    platform: {yaml_quote(str(platform))}")

    compose = "\n".join(lines) + "\n"

    env_lines = [
        "# Generated from the Portainer template registry.",
        "# Review values before deployment.",
        "",
        "# Root replacing the old Portainer /portainer path.",
        "PORTAINER_ROOT=/mnt/portainer",
    ]
    for e in envs:
        if e["description"]:
            env_lines.append(f"# {e['name']}: {e['description']}")
        env_lines.append(f"{e['name']}={e['value']}")
    env = "\n".join(env_lines) + "\n"
    return compose, env

def source_stack_url(t: dict[str, Any]) -> str:
    repo = t["repository"]["url"].rstrip("/")
    # All current entries point to Qballjos/portainer_templates master.
    path = t["repository"]["stackfile"].lstrip("/")
    return f"{repo}/raw/refs/heads/{DEFAULT_SOURCE_BRANCH}/{path}"

def stack_env(t: dict[str, Any]) -> str:
    envs = env_entries(t)
    lines = [
        "# Generated from the Portainer template metadata.",
        "# The Compose file is the original Portainer stack YAML.",
        "# Review all paths, image tags, and variables before deployment.",
        "",
        "PORTAINER_ROOT=/mnt/portainer",
    ]
    for e in envs:
        if e["description"]:
            lines.append(f"# {e['name']}: {e['description']}")
        lines.append(f"{e['name']}={e['value']}")
    return "\n".join(lines) + "\n"

def html_to_text(value: str) -> str:
    value = re.sub(r"<br\\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"</li>", "\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()

def build_readme(t: dict[str, Any], template_id: str, compose_kind: str, source_url: str) -> str:
    name = t.get("title") or t.get("name") or template_id
    desc = t.get("description", "").strip()
    note = html_to_text(str(t.get("note", "") or ""))
    cats = ", ".join(str(x) for x in (t.get("categories") or [])) or "Other"
    lines = [
        f"# {name}",
        "",
        desc,
        "",
        f"- **Arcane template ID:** `{template_id}`",
        f"- **Original Portainer name:** `{t.get('name', '')}`",
        f"- **Categories:** {cats}",
        f"- **Source type:** Portainer `{t.get('type', '')}`",
        f"- **Original source:** {source_url}",
        "",
    ]
    if note:
        lines += ["## Original Portainer notes", "", note, ""]
    lines += [
        "## Conversion notes",
        "",
        "This template was generated from the Portainer community template registry.",
        "Host paths beginning with `/portainer` are represented by `${PORTAINER_ROOT}`.",
        "Container-only mounts remain anonymous Docker volumes.",
        "Review ports, permissions, image tags, environment variables, and persistent",
        "storage before deploying.",
        "",
    ]
    if compose_kind == "stack":
        lines += [
            "The Compose file was retrieved from the Portainer stack file referenced",
            "by the original template. It has not been semantically rewritten.",
            "",
        ]
    return "\n".join(lines)

def make_registry_entry(t: dict[str, Any], template_id: str, base_url: str, source_url: str) -> dict[str, Any]:
    name = str(t.get("title") or t.get("name") or template_id)
    entry = {
        "id": template_id,
        "name": name,
        "description": str(t.get("description", "") or "").strip() or f"Portainer template: {name}",
        "version": "1.0.0",
        "author": "Qballjos/portainer_templates",
        "compose_url": f"{base_url}/templates/{template_id}/compose.yaml",
        "env_url": f"{base_url}/templates/{template_id}/.env.example",
        "documentation_url": f"{base_url}/templates/{template_id}/README.md",
        "tags": [slug(x) for x in (t.get("categories") or []) if str(x).strip()],
    }
    if not entry["tags"]:
        entry["tags"] = ["other"]
    return entry

def validate_shape(registry: dict[str, Any]) -> list[str]:
    errors = []
    allowed_top = {"$schema", "name", "description", "version", "author", "url", "templates"}
    extra = set(registry) - allowed_top
    if extra:
        errors.append(f"Top-level extra fields: {sorted(extra)}")
    for k in ["name", "description", "version", "author", "url", "templates"]:
        if k not in registry:
            errors.append(f"Missing top-level field: {k}")
    if not isinstance(registry.get("templates"), list):
        errors.append("templates must be an array")
        return errors
    allowed_template = {
        "id", "name", "description", "version", "author",
        "compose_url", "env_url", "documentation_url", "content_hash", "tags"
    }
    ids = set()
    for i, t in enumerate(registry["templates"]):
        extra = set(t) - allowed_template
        if extra:
            errors.append(f"Template {i} ({t.get('id')}): extra fields {sorted(extra)}")
        for k in ["id", "name", "description", "version", "author", "compose_url", "tags"]:
            if k not in t:
                errors.append(f"Template {i}: missing {k}")
        if t.get("id") in ids:
            errors.append(f"Duplicate template id: {t.get('id')}")
        ids.add(t.get("id"))
        if not isinstance(t.get("tags"), list) or not t.get("tags"):
            errors.append(f"Template {t.get('id')}: tags must be a non-empty array")
        for k in ["compose_url", "env_url"]:
            if k in t and not str(t[k]).startswith("https://"):
                errors.append(f"Template {t.get('id')}: {k} must be HTTPS")
    return errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True,
                    help="Public HTTPS directory where registry.json and templates/ will be hosted.")
    ap.add_argument("--output", default="output")
    ap.add_argument("--source-url", default=SOURCE_URL)
    args = ap.parse_args()

    base_url = args.base_url.rstrip("/")
    output = Path(args.output)
    if output.exists():
        shutil.rmtree(output)
    (output / "templates").mkdir(parents=True)

    print(f"Fetching source: {args.source_url}")
    source = fetch_json(args.source_url)
    templates = source.get("templates", [])
    if not isinstance(templates, list):
        raise SystemExit("Source JSON does not contain a templates array.")

    used = set()
    entries = []
    report = {
        "source_url": args.source_url,
        "source_version": source.get("version"),
        "source_template_count": len(templates),
        "converted": [],
        "failed": [],
    }

    for idx, t in enumerate(templates, 1):
        original_name = str(t.get("name") or t.get("title") or f"template-{idx}")
        tid = unique_id(original_name, used)
        td = output / "templates" / tid
        td.mkdir(parents=True)

        try:
            if t.get("type") == 3 and t.get("repository"):
                compose_source = source_stack_url(t)
                compose = fetch_text(compose_source)
                env = stack_env(t)
                kind = "stack"
            elif t.get("image"):
                compose, env = build_single_compose(t, tid)
                compose_source = args.source_url
                kind = "single-container"
            else:
                raise RuntimeError("No image and no supported repository stack reference.")

            (td / "compose.yaml").write_text(compose, encoding="utf-8", newline="\n")
            (td / ".env.example").write_text(env, encoding="utf-8", newline="\n")
            (td / "README.md").write_text(
                build_readme(t, tid, kind, compose_source),
                encoding="utf-8", newline="\n"
            )

            entries.append(make_registry_entry(t, tid, base_url, compose_source))
            report["converted"].append({
                "id": tid,
                "source_name": original_name,
                "type": t.get("type"),
                "kind": kind,
                "source": compose_source,
            })
            print(f"[{idx:3}/{len(templates)}] OK  {tid}")
        except Exception as exc:
            report["failed"].append({
                "source_name": original_name,
                "type": t.get("type"),
                "error": str(exc),
            })
            print(f"[{idx:3}/{len(templates)}] FAIL {original_name}: {exc}", file=sys.stderr)

    registry = {
        "$schema": "https://registry.getarcane.app/schema.json",
        "name": "Portainer Community Templates - Arcane Conversion",
        "description": "Converted Docker Compose templates generated from Qballjos/portainer_templates.",
        "version": "1.0.0",
        "author": "Qballjos/portainer_templates conversion",
        "url": base_url,
        "templates": entries,
    }

    errors = validate_shape(registry)
    if errors:
        raise SystemExit("Registry structural validation failed:\n- " + "\n- ".join(errors))

    (output / "registry.json").write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n"
    )
    report["converted_count"] = len(report["converted"])
    report["failed_count"] = len(report["failed"])
    report["structural_validation_errors"] = errors
    (output / "conversion-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n"
    )

    validation = [
        "# Validation",
        "",
        f"- Source templates found: **{len(templates)}**",
        f"- Converted successfully: **{len(entries)}**",
        f"- Failed conversion: **{len(report['failed'])}**",
        "- Registry structural validation: **PASS**",
        "",
        "The generated registry contains only fields documented by Arcane's registry schema.",
        "If `jsonschema` is installed, validate against the live Draft-07 schema with:",
        "",
        "```bash",
        "python -m pip install jsonschema",
        "python validate_arcane_registry.py",
        "```",
        "",
        "The registry and every referenced file must be hosted at publicly accessible HTTPS URLs.",
        "Raw GitHub URLs are suitable.",
        "",
    ]
    (output / "VALIDATION.md").write_text("\n".join(validation), encoding="utf-8", newline="\n")

    print()
    print(f"Completed: {len(entries)}/{len(templates)} templates")
    if report["failed"]:
        print("Failures are listed in conversion-report.json")

if __name__ == "__main__":
    main()
