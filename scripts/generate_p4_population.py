#!/usr/bin/env python3
"""CR-IS-CAT-02C-P4. Deterministic generator for the P4 vendor-neutral component
population of the ISC catalogue.

Emits and updates, relative to the repository root (default: the parent of
this directory):

- entities/v1-alpha/components/<domain>/components/<dir>/component.yaml  (new)
- entities/v1-alpha/components/<domain>/components/<dir>/README.md       (new)
- entities/v1-alpha/components/<domain>/index.yaml   (updated; P4 rows merged)
- entities/v1-alpha/index.yaml                       (updated; P4 counts merged)

The generator is idempotent and deterministic (per G-10): re-running it against
the same repository state reproduces byte-identical files. The P4 component
inventory is read from scripts/p4_component_data.json.

Usage: python3 scripts/generate_p4_population.py [repo_root]
"""

from __future__ import annotations
import json
import os
import re
import sys

CR = "CR-IS-CAT-02C-P4"
DATE = "2026-11-10"
PREFIX = "dea:information-system-component-"


# ---------------------------------------------------------------------------
# YAML emission helpers (stdlib only; no third-party dependencies).
# ---------------------------------------------------------------------------

def ystr(s):
    """Quote a string scalar conservatively for YAML."""
    s = str(s)
    reserved = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}
    scalar_like = (
        re.fullmatch(r"-?\d+(\.\d+)?", s)
        or re.fullmatch(r"\d{4}-\d{2}-\d{2}", s)
    )
    safe = (
        s != ""
        and not s[0].isspace()
        and not s[-1].isspace()
        and not s[0] in "!&*?|>%@`#\"'"
        and ": " not in s
        and " #" not in s
        and "\n" not in s
    )
    if safe and not scalar_like and s.lower() not in reserved:
        return s
    return "'" + s.replace("'", "''") + "'"


def emit_component_yaml(c):
    out = []
    out.append(f"id: {c['id']}")
    out.append(f"type: {c['type']}")
    out.append(f"name: {ystr(c['name'])}")
    out.append("status: active")
    out.append('version: "1.0"')
    out.append(f'effective_date: "{DATE}"')
    out.append("")
    out.append(f"f_level: {c['f_level']}")
    out.append("")
    out.append(f"component_domain: {ystr(c['domain_id'])}")
    out.append("")
    out.append("facets:")
    out.append(f"  component_kind: {c['kind']}")
    out.append("")
    if c.get("parent"):
        out.append(f"parent: {c['parent']}")
        out.append("")
    if c.get("composition"):
        out.append("composition:")
        for t in c["composition"]:
            out.append(f"  - target: {t}")
            out.append("    kind: contains")
            out.append("    cardinality: required")
            out.append('    version: "1.0"')
            out.append(f'    effective_date: "{DATE}"')
            out.append("    status: active")
        out.append("")
    out.append("readme: ./README.md")
    out.append("")
    return "\n".join(out)


F_LABEL = {"F0": "system", "F1": "component group", "F2": "composite component"}


def emit_component_readme(c, fn_count):
    """19-section README per templates/README-template.md (CR-IS-CAT-02B)."""
    lvl = c["f_level"]
    r = []
    r.append(f"# {c['name']}")
    r.append("")
    r.append("# 1. Component name and identifier")
    r.append(f"- Component name: {c['name']}")
    r.append(f"- Identifier: `{c['id']}`")
    r.append("")
    r.append("# 2. Definition")
    r.append(c["definition"])
    r.append("")
    r.append("# 3. Purpose and scope")
    r.append(
        "This is a P4 vendor-neutral population record (CR-IS-CAT-02C-P4; the 5-CR "
        "programme population series). The P4 tranche admits generic component "
        "classes realized by commercial and open-source products from at least "
        "three distinct vendors; per G-12 no implementation-specific component is "
        "canonical. The record follows the F0-F5 decomposition model in "
        "docs/decomposition-guide.md."
    )
    r.append("")
    r.append("# 4. Component type")
    r.append(c["type"])
    r.append("")
    r.append("# 5. F-level assignment")
    r.append(lvl)
    r.append("")
    r.append("# 6. Component-domain assignment")
    r.append(f"`{c['domain_id']}`")
    r.append("")
    r.append("# 7. Orthogonal classification facets")
    r.append(f"- Component kind: {c['kind']}")
    r.append(
        "- Hosting model / execution characteristics / criticality / deployment "
        "pattern / security posture / automation characteristics: not asserted by "
        "the vendor-neutral record; these facets vary across the corroborating "
        "vendor implementations and are populated per-deployment in a follow-on CR."
    )
    r.append("")
    r.append("# 8. Composition (parent, children)")
    if c.get("parent"):
        r.append(f"- Parent: `{c['parent']}`")
    else:
        r.append("- Parent: (none; this is the system-class record)")
    if c.get("composition"):
        for t in c["composition"]:
            r.append(f"- Child: `{t}`")
    else:
        r.append("- Children: (none)")
    r.append("")
    r.append("# 9. Composition edges")
    if c.get("composition"):
        for t in c["composition"]:
            r.append(f"- `{t}`: contains (required)")
    else:
        r.append("- (none; the parent is recorded in the `parent` field)")
    r.append("")
    r.append("# 10. Functional realization (functions realized by this component)")
    if lvl == "F2":
        r.append(
            f"- Executes {fn_count} vendor-neutral function record(s) of the P4 "
            "population (CR-IS-CAT-01C-P4 in technehub-labs/dea-catalog-system-functions); "
            "each function record lists this component in `executing_components`."
        )
    else:
        r.append(
            "- The functions realized by this " + F_LABEL[lvl] + " are recorded on "
            "its descendant components; see the descendant records and the ISF "
            "catalogue (CR-IS-CAT-01C-P4 executing_components crawl)."
        )
    r.append("")
    r.append("# 11. Cross-references (components related by other metamodel relationships)")
    r.append("- (none in this CR; cross-catalogue relationships remain owned by CR-IS-CAT-02D)")
    r.append("")
    r.append("# 12. Hosting and deployment")
    r.append(
        "The hosting model is not asserted by the vendor-neutral record; the generic "
        "class is commonly offered as cloud, on-premises or hybrid deployments across "
        "the corroborating vendors. The hosting facet is populated per-deployment."
    )
    r.append("")
    r.append("# 13. Criticality and security posture")
    r.append(
        "Criticality and security posture facets are not asserted by the "
        "vendor-neutral record; they are populated per-deployment once the "
        "criticality class is asserted."
    )
    r.append("")
    r.append("# 14. Performance characteristics")
    r.append(
        "Performance characteristics are vendor-deployment-specific and are not "
        "asserted by the vendor-neutral record."
    )
    r.append("")
    r.append("# 15. Disaster recovery posture")
    r.append(
        "The disaster recovery posture is captured by the standard RTO/RPO values per "
        "criticality class once the criticality facet is asserted per-deployment: "
        "mission-critical RTO 15 minutes / RPO 5 minutes; business-critical RTO 4 "
        "hours / RPO 1 hour; supporting RTO 24 hours / RPO 24 hours."
    )
    r.append("")
    r.append("# 16. Compliance posture")
    r.append("Compliance posture is context-specific and is populated per-record in subsequent CRs.")
    r.append("")
    r.append("# 17. Owner")
    r.append("Enterprise Architecture team (DEA-Architecture@example.com)")
    r.append("")
    r.append("# 18. Change history")
    r.append(f"- 1.0: {DATE}: Initial P4 vendor-neutral record ({CR}).")
    r.append("")
    r.append("# 19. References")
    r.append("- `change-requests/CR-IS-CAT-02C-P4-vendor-neutral-component-population.md` (the CR doc)")
    r.append("- `docs/coverage-reports/p4-coverage-report.md` (the P4 coverage report)")
    r.append("- `docs/decomposition-guide.md` (the F0-F5 model)")
    r.append("- `taxonomy/` (the classification layer)")
    r.append("- `schemas/entities/information-system-component.v2.json` (the v2 schema)")
    r.append("- `technehub-labs/dea-catalog-system-functions` (the executing-function catalogue; CR-IS-CAT-01C-P4)")
    r.append("")
    return "\n".join(r)


# ---------------------------------------------------------------------------
# Domain index merge (line-based; the domain index files are simple mappings).
# ---------------------------------------------------------------------------

def parse_domain_index(text):
    """Return (pre_lines, entries, ch_lines) for a domain index file.

    pre_lines: everything up to and including the 'components:' marker.
    entries:   list of dicts (id/name/f_level/type/path keys).
    ch_lines:  the change_history block (from its marker to EOF).
    """
    lines = text.split("\n")
    entries = []
    i = 0
    comp_at = None
    ch_at = None
    while i < len(lines):
        if lines[i].startswith("components:"):
            comp_at = i
            i += 1
            cur = None
            while i < len(lines) and (lines[i].startswith("  - ") or lines[i].startswith("    ")):
                if lines[i].startswith("  - "):
                    if cur is not None:
                        entries.append(cur)
                    cur = {}
                    k, _, v = lines[i][4:].partition(": ")
                    cur[k] = v
                else:
                    k, _, v = lines[i].strip().partition(": ")
                    cur[k] = v
                i += 1
            if cur is not None:
                entries.append(cur)
            continue
        if lines[i].startswith("change_history:"):
            ch_at = i
            break
        i += 1
    return lines[: (comp_at + 1) if comp_at is not None else 0], entries, lines[ch_at:]


def merge_domain_index(ipath, dcomps):
    with open(ipath) as f:
        text = f.read()
    pre, entries, ch = parse_domain_index(text)
    p4_ids = {c["id"] for c in dcomps}
    kept = [e for e in entries if e["id"] not in p4_ids]
    final = kept + [
        {k: c[k] for k in ("id", "name", "f_level", "type")} for c in sorted(dcomps, key=lambda c: c["id"])
    ]
    out = list(pre)
    for e in final:
        out.append(f"  - id: {e['id']}")
        out.append(f"    name: {ystr(e['name'])}")
        out.append(f"    f_level: {e['f_level']}")
        out.append(f"    type: {e['type']}")
        out.append("    status: active")
        out.append(f"    path: components/{e['id'].split(':')[-1]}/")
    out.append("")
    if not any(CR in ln for ln in ch):
        while ch and ch[-1] == "":
            ch.pop()
        ch.append('  - version: "1.1"')
        ch.append(f"    date: {DATE}")
        ch.append(f"    cr: {CR}")
        ch.append(
            f'    note: "P4 vendor-neutral component population. {len(dcomps)} '
            f'records added. Total domain records: {len(final)}."'
        )
        ch.append("")
    out.extend(ch)
    with open(ipath, "w") as f:
        f.write("\n".join(out))


def merge_root_index(rpath, by_domain, n_components):
    with open(rpath) as f:
        text = f.read()
    has_p4 = CR in text
    if not has_p4:
        for dslug, dcomps in by_domain.items():
            n = len(dcomps)
            pat = re.compile(
                r"(- id: iscc:domain:" + re.escape(dslug) + r"\n(?:.*\n)*?    component_count: )(\d+)"
            )
            m = pat.search(text)
            if m:
                text = text[: m.start(2)] + str(int(m.group(2)) + n) + text[m.end(2):]
        m = re.search(r"total_components: (\d+)", text)
        total = int(m.group(1)) + n_components if m else n_components
        if m:
            text = text[: m.start(1)] + str(total) + text[m.end(1):]
        fdist = {"F0": 0, "F1": 0, "F2": 0, "F3": 0, "F4": 0, "F5": 0}
        for c in (x for comps in by_domain.values() for x in comps):
            fdist[c["f_level"]] += 1
        for lvl in fdist:
            mm = re.search(rf"(  {lvl}: )(\d+)", text)
            if mm:
                text = text[: mm.start(2)] + str(int(mm.group(2)) + fdist[lvl]) + text[mm.end(2):]
        mm = re.search(r"change_history:\n", text)
        if mm:
            entry = (
                f'  - version: "1.3"\n'
                f"    date: {DATE}\n"
                f"    cr: {CR}\n"
                f'    note: "P4 vendor-neutral component population. {n_components} '
                f"generic component records added ({fdist['F0']} F0 system classes + "
                f"{fdist['F1']} F1 component groups + {fdist['F2']} F2 composite "
                f"components) across {len(by_domain)} of 10 ISCC domains. Vendor "
                f"products are evidence only per G-12. Total catalog: {total} "
                f'records."\n'
            )
            text = text[: mm.end()] + entry + text[mm.end():]
        with open(rpath, "w") as f:
            f.write(text)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    data_path = os.path.join(here, "p4_component_data.json")
    if not os.path.exists(data_path):
        data_path = os.path.join(repo, "scripts", "p4_component_data.json")
    data = json.load(open(data_path))

    comps = data["components"]
    fn_by_f2 = data.get("function_counts", {})
    by_domain = {}
    for c in comps:
        c = dict(c)
        c["domain_id"] = f"iscc:domain:{c['domain_slug']}"
        by_domain.setdefault(c["domain_slug"], []).append(c)
        dirn = c["id"].split(":")[-1]  # full id suffix (governance glob requires it)
        base = os.path.join(repo, "entities", "v1-alpha", "components",
                            c["domain_slug"], "components", dirn)
        os.makedirs(base, exist_ok=True)
        fc = fn_by_f2.get(c["id"], 0) if c["f_level"] == "F2" else 0
        with open(os.path.join(base, "component.yaml"), "w") as f:
            f.write(emit_component_yaml(c))
        with open(os.path.join(base, "README.md"), "w") as f:
            f.write(emit_component_readme(c, fc))

    for dslug, dcomps in by_domain.items():
        merge_domain_index(
            os.path.join(repo, "entities", "v1-alpha", "components", dslug, "index.yaml"),
            dcomps,
        )
    merge_root_index(os.path.join(repo, "entities", "v1-alpha", "index.yaml"),
                     by_domain, len(comps))

    fdist = {"F0": 0, "F1": 0, "F2": 0}
    for c in comps:
        fdist[c["f_level"]] += 1
    print(f"OK: {CR} emitted {len(comps)} component records "
          f"({fdist['F0']} F0 + {fdist['F1']} F1 + {fdist['F2']} F2) across "
          f"{len(by_domain)} domains (repo root: {repo})")


if __name__ == "__main__":
    main()
