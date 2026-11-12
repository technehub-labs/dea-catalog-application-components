#!/usr/bin/env python3
"""CR-IS-CAT-02C-P5. Deterministic generator for the P5 atomic-component
population of the ISC catalogue.

Emits and updates, relative to the repository root (default: the parent of
this directory):

- entities/v1-alpha/components/<domain>/components/<dir>/component.yaml  (new, F3 atoms)
- entities/v1-alpha/components/<domain>/components/<dir>/README.md       (new)
- entities/v1-alpha/components/<domain>/components/<f2-dir>/component.yaml (updated; composition appended)
- entities/v1-alpha/components/<domain>/components/<f2-dir>/README.md      (updated; sections 8, 9, 10, 18, 19)
- entities/v1-alpha/components/<domain>/index.yaml   (updated; P5 rows merged)
- entities/v1-alpha/index.yaml                       (updated; P5 counts merged)

The generator is idempotent and deterministic (per G-10): re-running it against
the same repository state reproduces byte-identical files. The P5 atom
inventory is read from scripts/p5_component_data.json, which records the
canonical verb-cluster decomposition of the CR-IS-CAT-01C-P4 function
population over the CR-IS-CAT-02C-P4 F2 composite components.

Usage: python3 scripts/generate_p5_population.py [repo_root]
"""

from __future__ import annotations
import json
import os
import re
import sys

CR = "CR-IS-CAT-02C-P5"
CR_P4 = "CR-IS-CAT-02C-P4"
DATE = "2026-11-12"


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


def emit_atom_yaml(a):
    out = []
    out.append(f"id: {a['id']}")
    out.append(f"type: {a['type']}")
    out.append(f"name: {ystr(a['name'])}")
    out.append("status: active")
    out.append('version: "1.0"')
    out.append(f'effective_date: "{DATE}"')
    out.append("")
    out.append("f_level: F3")
    out.append("")
    out.append(f"component_domain: {ystr('iscc:domain:' + a['domain_slug'])}")
    out.append("")
    out.append("facets:")
    out.append(f"  component_kind: {a['kind']}")
    out.append("")
    out.append(f"parent: {a['parent']}")
    out.append("")
    out.append("readme: ./README.md")
    out.append("")
    return "\n".join(out)


def emit_atom_readme(a):
    """19-section README per templates/README-template.md (CR-IS-CAT-02B)."""
    r = []
    r.append(f"# {a['name']}")
    r.append("")
    r.append("# 1. Component name and identifier")
    r.append(f"- Component name: {a['name']}")
    r.append(f"- Identifier: `{a['id']}`")
    r.append("")
    r.append("# 2. Definition")
    r.append(a["definition"])
    r.append("")
    r.append("# 3. Purpose and scope")
    r.append(
        "This is a P5 atomic decomposition record (CR-IS-CAT-02C-P5; the 5-CR "
        "programme population series). The P5 tranche decomposes each P4 "
        "composite component into F3 atomic components via the canonical "
        "verb-cluster taxonomy of its CR-IS-CAT-01C-P4 function names; per "
        "G-12 no implementation-specific component is canonical. The record "
        "follows the F0-F5 decomposition model in docs/decomposition-guide.md."
    )
    r.append("")
    r.append("# 4. Component type")
    r.append(a["type"])
    r.append("")
    r.append("# 5. F-level assignment")
    r.append("F3")
    r.append("")
    r.append("# 6. Component-domain assignment")
    r.append(f"`iscc:domain:{a['domain_slug']}`")
    r.append("")
    r.append("# 7. Orthogonal classification facets")
    r.append(f"- Component kind: {a['kind']}")
    r.append(
        "- Hosting model / execution characteristics / criticality / deployment "
        "pattern / security posture / automation characteristics: not asserted by "
        "the vendor-neutral record; these facets vary across the corroborating "
        "vendor implementations and are populated per-deployment in a follow-on CR."
    )
    r.append("")
    r.append("# 8. Composition (parent, children)")
    r.append(f"- Parent: `{a['parent']}`")
    r.append("- Children: (none)")
    r.append("")
    r.append("# 9. Composition edges")
    r.append("- (none; the parent is recorded in the `parent` field)")
    r.append("")
    r.append("# 10. Functional realization (functions realized by this component)")
    r.append(
        f"This atomic component realizes the {a['cluster_title']} verb cluster: it "
        f"{a['cluster_definition']}. It executes the {len(a['function_ids'])} P4 "
        "function record(s) listed below (CR-IS-CAT-01C-P4 in "
        "technehub-labs/dea-catalog-system-functions); each function record lists "
        "the parent composite component in `executing_components`."
    )
    for fid, fname in zip(a["function_ids"], a["function_names"]):
        r.append(f"- `{fid}`: {fname}")
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
    r.append(f"- 1.0: {DATE}: Initial P5 atomic record ({CR}).")
    r.append("")
    r.append("# 19. References")
    r.append("- `change-requests/CR-IS-CAT-02C-P5-atomic-component-population.md` (the CR doc)")
    r.append("- `docs/coverage-reports/p5-coverage-report.md` (the P5 coverage report)")
    r.append("- `docs/decomposition-guide.md` (the F0-F5 model)")
    r.append("- `taxonomy/` (the classification layer)")
    r.append("- `schemas/entities/information-system-component.v2.json` (the v2 schema)")
    r.append("- `technehub-labs/dea-catalog-system-functions` (the executing-function catalogue; CR-IS-CAT-01C-P4)")
    r.append("- `change-requests/CR-IS-CAT-02C-P4-vendor-neutral-component-population.md` (the parent P4 population)")
    r.append("")
    return "\n".join(r)


# ---------------------------------------------------------------------------
# P4 F2 record and README updates (deterministic in-place edits).
# ---------------------------------------------------------------------------

def composition_block(child_ids):
    out = ["composition:"]
    for cid in child_ids:
        out.append(f"  - target: {cid}")
        out.append("    kind: contains")
        out.append("    cardinality: required")
        out.append('    version: "1.0"')
        out.append(f'    effective_date: "{DATE}"')
        out.append("    status: active")
    return "\n".join(out)


def update_f2_record(path, child_ids):
    """Insert the P5 composition block between `parent:` and `readme:`.

    P4 F2 records have no composition block (their children did not exist at
    P4 time); the P5 atoms are their first children, so the block is inserted
    once. Idempotent: if a composition block is already present, the record
    is left untouched.
    """
    with open(path) as f:
        text = f.read()
    if "\ncomposition:\n" in text or text.startswith("composition:"):
        return False
    marker = "\nreadme: ./README.md"
    assert marker in text, f"unexpected record shape: {path}"
    block = composition_block(child_ids)
    text = text.replace(marker, "\n" + block + "\n" + marker, 1)
    with open(path, "w") as f:
        f.write(text)
    return True


def update_f2_readme(path, child_ids):
    """Update sections 8, 9, 10, 18 and 19 of a P4 F2 README. Idempotent."""
    with open(path) as f:
        text = f.read()
    changed = False
    if "# 8." in text and "- Children: (none)" in text:
        child_lines = "".join(f"- Child: `{cid}`\n" for cid in child_ids)
        text = text.replace("- Children: (none)\n", child_lines, 1)
        changed = True
    if "# 9." in text and "- (none; the parent is recorded in the `parent` field)" in text:
        edge_lines = "".join(f"- `{cid}`: contains (required)\n" for cid in child_ids)
        text = text.replace(
            "- (none; the parent is recorded in the `parent` field)\n", edge_lines, 1
        )
        changed = True
    if "via the canonical verb-cluster taxonomy of its P4 function names" not in text:
        anchor = None
        for line in text.split("\n"):
            if line.startswith("- Executes ") and "vendor-neutral function record" in line:
                anchor = line
                break
        assert anchor, f"no functional-realization anchor in {path}"
        addendum = (
            f"{anchor}\n- Decomposed by {CR} into {len(child_ids)} F3 atomic "
            "components via the canonical verb-cluster taxonomy of its P4 "
            "function names; see the child records."
        )
        text = text.replace(anchor + "\n", addendum + "\n", 1)
        changed = True
    if f"- 1.1: {DATE}: P5 atomic decomposition" not in text:
        hist_anchor = f"- 1.0: 2026-11-10: Initial P4 vendor-neutral record ({CR_P4})."
        assert hist_anchor in text, f"no change-history anchor in {path}"
        text = text.replace(
            hist_anchor + "\n",
            f"{hist_anchor}\n- 1.1: {DATE}: P5 atomic decomposition ({CR}): "
            f"{len(child_ids)} F3 atomic components attached.\n",
            1,
        )
        changed = True
    if "CR-IS-CAT-02C-P5-atomic-component-population.md" not in text:
        text = text.rstrip("\n") + "\n"
        text += (
            "- `change-requests/CR-IS-CAT-02C-P5-atomic-component-population.md` (the P5 CR doc)\n"
            "- `scripts/p5_component_data.json` (the P5 atom inventory)\n"
        )
        changed = True
    if changed:
        with open(path, "w") as f:
            f.write(text)
    return changed


# ---------------------------------------------------------------------------
# Domain index merge (line-based; mirrors the P4 generator).
# ---------------------------------------------------------------------------

def parse_domain_index(text):
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
    p5_ids = {c["id"] for c in dcomps}
    kept = [e for e in entries if e["id"] not in p5_ids]
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
        ch.append('  - version: "1.2"')
        ch.append(f"    date: {DATE}")
        ch.append(f"    cr: {CR}")
        ch.append(
            f'    note: "P5 atomic-component population. {len(dcomps)} F3 '
            f'records added. Total domain records: {len(final)}."'
        )
        ch.append("")
    out.extend(ch)
    with open(ipath, "w") as f:
        f.write("\n".join(out))


def merge_root_index(rpath, by_domain, n_components):
    with open(rpath) as f:
        text = f.read()
    has_p5 = CR in text
    if not has_p5:
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
        mm = re.search(r"(  F3: )(\d+)", text)
        if mm:
            text = text[: mm.start(2)] + str(int(mm.group(2)) + n_components) + text[mm.end(2):]
        mm = re.search(r"change_history:\n", text)
        if mm:
            entry = (
                f'  - version: "1.4"\n'
                f"    date: {DATE}\n"
                f"    cr: {CR}\n"
                f'    note: "P5 atomic-component population. {n_components} F3 '
                f"atomic component records added via the canonical verb-cluster "
                f"decomposition of the {CR_P4} F2 composite components "
                f"(source: CR-IS-CAT-01C-P4 function names in the ISF catalogue) "
                f"across {len(by_domain)} of 10 ISCC domains. Vendor products are "
                f"evidence only per G-12. Total catalog: {total} records.\"\n"
            )
            text = text[: mm.end()] + entry + text[mm.end():]
        with open(rpath, "w") as f:
            f.write(text)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    data_path = os.path.join(here, "p5_component_data.json")
    if not os.path.exists(data_path):
        data_path = os.path.join(repo, "scripts", "p5_component_data.json")
    data = json.load(open(data_path))

    atoms = data["atoms"]
    assert all(a["id"].startswith(a["parent"] + "-") for a in atoms), "atom id must extend parent id"
    by_domain = {}
    by_parent = {}
    for a in atoms:
        by_domain.setdefault(a["domain_slug"], []).append(a)
        by_parent.setdefault(a["parent"], []).append(a)

    # 1. Emit the F3 atom records and READMEs.
    for a in atoms:
        dirn = a["id"].split(":")[-1]
        base = os.path.join(repo, "entities", "v1-alpha", "components",
                            a["domain_slug"], "components", dirn)
        os.makedirs(base, exist_ok=True)
        with open(os.path.join(base, "component.yaml"), "w") as f:
            f.write(emit_atom_yaml(a))
        with open(os.path.join(base, "README.md"), "w") as f:
            f.write(emit_atom_readme(a))

    # 2. Update the 141 P4 F2 parents (composition + README sections).
    updated = 0
    for f2_id, kids in sorted(by_parent.items()):
        kid_ids = sorted(k["id"] for k in kids)
        dirn = f2_id.split(":")[-1]
        found = False
        for domain in os.listdir(os.path.join(repo, "entities", "v1-alpha", "components")):
            cand = os.path.join(repo, "entities", "v1-alpha", "components", domain,
                                "components", dirn)
            if os.path.isdir(cand):
                update_f2_record(os.path.join(cand, "component.yaml"), kid_ids)
                update_f2_readme(os.path.join(cand, "README.md"), kid_ids)
                updated += 1
                found = True
                break
        assert found, f"F2 directory not found for {f2_id}"

    # 3. Domain-level and catalog-level index merges.
    for dslug, dcomps in by_domain.items():
        merge_domain_index(
            os.path.join(repo, "entities", "v1-alpha", "components", dslug, "index.yaml"),
            dcomps,
        )
    merge_root_index(os.path.join(repo, "entities", "v1-alpha", "index.yaml"),
                     by_domain, len(atoms))

    cdist = {}
    for a in atoms:
        cdist[a["cluster"]] = cdist.get(a["cluster"], 0) + 1
    print(f"OK: {CR} emitted {len(atoms)} F3 atomic component records across "
          f"{len(by_domain)} domains; updated {updated} P4 F2 parent records "
          f"(repo root: {repo})")


if __name__ == "__main__":
    main()
