import json
import os
import re

# Load data
with open('deep_analysis.json', 'r') as f:
    data = json.load(f)
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)
with open('intelligence_results.json', 'r') as f:
    intel = json.load(f)

base_dir = "Constitutional Reviews/Discovery/"

def clean_id(did):
    return did.split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')

def write_report(filename, title, content):
    with open(os.path.join(base_dir, filename), 'w') as f:
        f.write(f"# {title}\n\n{content}")

# 00_MISSION_EXECUTIVE_SUMMARY.md
write_report("00_MISSION_EXECUTIVE_SUMMARY.md", "00 MISSION EXECUTIVE SUMMARY",
"## 1. Discovery & Intelligence Overview\n"
f"- **Total Constitutional Artifacts Mapped:** {len(data)}\n"
"- **Canonical Authority Analysis:** All documents tiered into Foundations, Constitution, Capabilities, Runtime, Supporting, and Archive.\n\n"
"## 2. Migration Assessment Summary\n"
"- **Directory Restructure:** Proposed ideal ZRMv3 layout (Report 09).\n"
"- **Migration Plan:** Detailed file-by-file execution checklist (Report 10).\n"
"- **Health Score:** Repository integrity evaluated at Tier 2 (Average 6/10), requiring systematic cleanup (Report 17).\n\n"
"## 3. Key Findings\n"
"- **Semantic Debt:** Multiple conflicting definitions for core concepts (Identity, Reality) found across layers.\n"
"- **Knowledge Gaps:** Critical missing dependencies identified for FED and Marketplace specifications.\n"
"- **Orphan Proliferation:** Significant volume of disconnected artifacts discovered in RTC and legacy folders.\n")

# 01_DOCUMENT_REGISTRY.md
registry = "| ID | Title | Authority Score | Status | Path |\n| --- | --- | --- | --- | --- |\n"
for d in data:
    registry += f"| {clean_id(d['doc_id'])} | {d['title']} | {d['authority_score']} | {d['status']} | {d['file_path']} |\n"
write_report("01_DOCUMENT_REGISTRY.md", "01 DOCUMENT REGISTRY", registry)

# 02_CONSTITUTIONAL_HIERARCHY.md
hierarchy = ""
layers = {}
for d in data:
    score = d['authority_score']
    if score not in layers: layers[score] = []
    layers[score].append(d)
for layer, docs in sorted(layers.items()):
    hierarchy += f"## {layer}\n"
    for d in docs:
        hierarchy += f"- **{clean_id(d['doc_id'])}**: {d['title']} ({d['file_path']})\n"
    hierarchy += "\n"
write_report("02_CONSTITUTIONAL_HIERARCHY.md", "02 CONSTITUTIONAL HIERARCHY", hierarchy)

# 03_DEPENDENCY_GRAPH.md
dep_graph = "```mermaid\ngraph TD\n"
for d in data:
    did = clean_id(d['doc_id'])
    if did != "Unknown":
        for dep in d['depends_on']:
            dep_graph += f"  {did} --> {dep}\n"
dep_graph += "```"
write_report("03_DEPENDENCY_GRAPH.md", "03 DEPENDENCY GRAPH", dep_graph)

# 04_CITATION_INDEX.md
citations = "| Source | Referenced Doc | Sections |\n| --- | --- | --- |\n"
for d in data:
    source = clean_id(d['doc_id'])
    refs = ", ".join(d['doc_refs'][:10])
    sects = ", ".join(d['section_refs'][:5])
    citations += f"| {source} | {refs} | {sects} |\n"
write_report("04_CITATION_INDEX.md", "04 CITATION INDEX", citations)

# 05_CONCEPT_INDEX.md
concept_idx = "| Concept | Owner | Authority Score | Definition |\n| --- | --- | --- | --- |\n"
for c, cdata in sorted(concepts.items()):
    score = "Unknown"
    for d in data:
        if d['file_path'] == cdata['owning_document']:
            score = d['authority_score']
            break
    concept_idx += f"| {c} | {cdata['owning_document']} | {score} | {cdata['definition']} |\n"
write_report("05_CONCEPT_INDEX.md", "05 CONCEPT INDEX", concept_idx)

# 06_DOCUMENT_SUMMARIES.md
summaries = ""
for d in data:
    summaries += f"## {clean_id(d['doc_id'])}: {d['title']}\n\n"
    summaries += f"- **Purpose:** {d['purpose']}\n"
    summaries += f"- **File Path:** {d['file_path']}\n"
    summaries += f"- **Dependencies:** {', '.join(d['depends_on'])}\n"
    summaries += f"- **Status:** {d['status']} ({d['version']})\n\n"
write_report("06_DOCUMENT_SUMMARIES.md", "06 DOCUMENT SUMMARIES", summaries)

# 07_KNOWLEDGE_GRAPH.md
k_graph = "```mermaid\ngraph LR\n"
for concept in ["REALITY", "INTENT", "TRUST", "ACTOR", "IDENTITY", "REFERENT", "SURFACE", "OBSERVER", "EVENT", "EVIDENCE"]:
    if concept in concepts:
        doc_id = clean_id(concepts[concept]['owning_document'].split('/')[-1].replace('.md', ''))
        k_graph += f"  {concept}([Concept: {concept}]) --> {doc_id}\n"
k_graph += "```"
write_report("07_KNOWLEDGE_GRAPH.md", "07 KNOWLEDGE GRAPH", k_graph)

# 08_DISCOVERY_FINDINGS.md
findings = "## 1. Document Families Discovered\n- ZRM, WS, RI, RSN, CA, SDK, RTC, Economic, DJ, POL, SEC\n\n## 2. Anomalies\n- Version drift in North Star and Founding Principles.\n- Naming collisions for blueprints.\n- Orphaned RTC documents.\n"
write_report("08_DISCOVERY_FINDINGS.md", "08 DISCOVERY FINDINGS", findings)

# 09_DIRECTORY_RESTRUCTURE_PROPOSAL.md
restructure = """
## Ideal Repository Layout (/ZRMv3/)

### /00-Governance
- **Purpose:** Foundational rules and dossiers.
- **Naming:** GOV-NNN.md

### /01-Foundations
- **Purpose:** North Star and Axioms.
- **Naming:** FOUNDATION-NAME.md

### /02-Constitution
- **Purpose:** ZRM core ontology.
- **Naming:** ZRM-NNN.md

### /03-World-Specifications
- **Purpose:** 17 clusters of capability specifications.
- **Naming:** WS-NNN.md

### /04-Reasoning
- **Purpose:** Logic and reasoning protocols.
- **Naming:** RSN-NNN.md

### /05-Runtime
- **Purpose:** Executable specifications and compiler.
- **Naming:** RI-NNN.md

### /06-SDK
- **Purpose:** Interface contracts.
- **Naming:** SDK-SPEC-NNN.md

### /07-Security
- **Purpose:** Protection profiles.
- **Naming:** SEC-NNN.md

### /08-Policies
- **Purpose:** Policy directives.
- **Naming:** POL-NNN.md

### /09-Reference
- **Purpose:** Supporting docs.
- **Naming:** REF-NNN.md

### /10-Archive
- **Purpose:** Historical artifacts.
"""
write_report("09_DIRECTORY_RESTRUCTURE_PROPOSAL.md", "09 DIRECTORY RESTRUCTURE PROPOSAL", restructure)

# 10_MIGRATION_PLAN.md
mig_plan = "| Old Path | New Path | Action | Reason |\n| --- | --- | --- | --- |\n"
for d in data:
    old = d['file_path']
    score = d['authority_score']
    did = clean_id(d['doc_id'])
    folder = "10-Archive"
    if score == "Foundation": folder = "01-Foundations"
    elif score == "Constitutional": folder = "02-Constitution"
    elif score == "Capability": folder = "03-World-Specifications"
    elif score == "Runtime": folder = "05-Runtime"
    elif score == "Supporting": folder = "09-Reference"
    new = f"/ZRMv3/{folder}/{did}.md"
    if did == "Unknown": new = f"/ZRMv3/{folder}/{old.split('/')[-1]}"
    action = "Move" if score not in ["Archive", "Historical"] else "Archive"
    mig_plan += f"| {old} | {new} | {action} | Tier: {score} |\n"
write_report("10_MIGRATION_PLAN.md", "10 MIGRATION PLAN", mig_plan)

# 11_DUPLICATE_AND_SUPERSESSION_ANALYSIS.md
dup_analysis = ""
titles = {}
for d in data:
    t = d['title'].upper()
    if t not in titles: titles[t] = []
    titles[t].append(d)
for title, docs in titles.items():
    if len(docs) > 1 and title != "UNKNOWN":
        dup_analysis += f"### Entity: {title}\n"
        latest = docs[0]
        for doc in docs:
            if "/ratified/" in doc['file_path'].lower(): latest = doc
        dup_analysis += f"- **Authoritative:** {latest['file_path']}\n"
        dup_analysis += "- **Superseded:**\n"
        for doc in docs:
            if doc != latest: dup_analysis += f"  - {doc['file_path']}\n"
        dup_analysis += "\n"
write_report("11_DUPLICATE_AND_SUPERSESSION_ANALYSIS.md", "11 DUPLICATE AND SUPERSESSION ANALYSIS", dup_analysis)

# 12_CANONICAL_NAMING_STANDARD.md
naming_std = "| Family | Pattern | Example |\n| --- | --- | --- |\n| WS | WS-XX.Y.Z | WS-03A.1.md |\n| RI | RI-NNN | RI-001.md |\n| RSN | RSN-NNN | RSN-001.md |\n| ZRM | ZRM-NNN | ZRM-001.md |\n| SDK | SDK-SPEC-NNN | SDK-SPEC-001.md |\n"
write_report("12_CANONICAL_NAMING_STANDARD.md", "12 CANONICAL NAMING STANDARD", naming_std)

# 13_ORPHAN_ANALYSIS.md
orphan_list = "| ID | File Path | Authority Score |\n| --- | --- | --- |\n"
for o in intel['orphans']:
    orphan_list += f"| {clean_id(o['doc_id'])} | {o['file_path']} | {o['authority_score']} |\n"
write_report("13_ORPHAN_ANALYSIS.md", "13 ORPHAN ANALYSIS", orphan_list)

# 14_CONFLICT_ANALYSIS.md
conflict_list = ""
for concept, docs in intel['conflicts'].items():
    if len(docs) > 1:
        conflict_list += f"### {concept}\nDefined in:\n"
        for d in set(docs): conflict_list += f"- {d}\n"
        conflict_list += "\n"
write_report("14_CONFLICT_ANALYSIS.md", "14 CONFLICT ANALYSIS", conflict_list)

# 15_GAP_ANALYSIS.md
gap_list = "| Source | Missing Target |\n| --- | --- |\n"
for gap in intel['gaps']:
    gap_list += f"| {gap['source']} | {gap['target']} |\n"
write_report("15_GAP_ANALYSIS.md", "15 GAP ANALYSIS", gap_list)

# 16_AI_NAVIGATION_INDEX.md
ai_idx = ""
for d in data:
    ai_idx += f"### {clean_id(d['doc_id'])}\n- **Summary:** {d['purpose']}\n- **Depends on:** {', '.join(d['depends_on'])}\n- **Defines:** {', '.join(d.get('defines', []))}\n\n"
write_report("16_AI_NAVIGATION_INDEX.md", "16 AI NAVIGATION INDEX", ai_idx)

# 17_REPOSITORY_HEALTH_SCORE.md
health = "| Category | Score (0-10) | Recommendation |\n| --- | --- | --- |\n"
for cat, score in intel['health_scores'].items():
    health += f"| {cat} | {score} | See relevant report for cleanup. |\n"
write_report("17_REPOSITORY_HEALTH_SCORE.md", "17 REPOSITORY HEALTH SCORE", health)

# Add TOC and Related Links to all
reports = sorted(os.listdir(base_dir))
for r in reports:
    path = os.path.join(base_dir, r)
    with open(path, 'r') as f:
        content = f.read()

    related = "\n\n## Related Reports\n\n"
    for other in reports:
        if other != r:
            related += f"- [{other.replace('_', ' ').replace('.md', '')}]({other})\n"

    toc = ""
    if r in ["01_DOCUMENT_REGISTRY.md", "06_DOCUMENT_SUMMARIES.md", "10_MIGRATION_PLAN.md", "16_AI_NAVIGATION_INDEX.md"]:
        toc = "## Table of Contents\n\n"
        for line in content.split('\n'):
            if line.startswith('## ') or line.startswith('### '):
                h = line.strip('# ').strip()
                anchor = h.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('/', '')
                indent = "  " if line.startswith('### ') else ""
                toc += f"{indent}- [{h}](#{anchor})\n"
        toc += "\n---\n\n"

    final = content.split('\n')[0] + "\n\n" + toc + "\n".join(content.split('\n')[1:]) + related
    with open(path, 'w') as f:
        f.write(final)
