import json
import os

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

# Helper to clean Doc IDs
def clean_id(did):
    return did.split('**')[0].strip().replace('Document ID: ', '')

# 01_DOCUMENT_REGISTRY.md
with open('Constitutional Reviews/Discovery/01_DOCUMENT_REGISTRY.md', 'w') as f:
    f.write("# 01 DOCUMENT REGISTRY\n\n")
    f.write("| Document ID | Title | Version | Status | File Path | Author |\n")
    f.write("| --- | --- | --- | --- | --- | --- |\n")
    for d in data:
        f.write(f"| {clean_id(d['doc_id'])} | {d['title']} | {d['version']} | {d['status']} | {d['file_path']} | {d['author']} |\n")

# 03_DEPENDENCY_GRAPH.md
with open('Constitutional Reviews/Discovery/03_DEPENDENCY_GRAPH.md', 'w') as f:
    f.write("# 03 DEPENDENCY GRAPH\n\n")
    f.write("```mermaid\ngraph TD\n")
    for d in data:
        did = clean_id(d['doc_id'])
        if did != "Unknown":
            for dep in d['depends_on']:
                f.write(f"  {did} --> {dep}\n")
    f.write("```\n")

# 04_CITATION_INDEX.md
with open('Constitutional Reviews/Discovery/04_CITATION_INDEX.md', 'w') as f:
    f.write("# 04 CITATION INDEX\n\n")
    f.write("| Source | Referenced Doc | Sections |\n")
    f.write("| --- | --- | --- |\n")
    for d in data:
        source = clean_id(d['doc_id'])
        refs = ", ".join(d['doc_refs'][:10])
        sects = ", ".join(d['section_refs'][:5])
        f.write(f"| {source} | {refs} | {sects} |\n")

# 06_DOCUMENT_SUMMARIES.md
with open('Constitutional Reviews/Discovery/06_DOCUMENT_SUMMARIES.md', 'w') as f:
    f.write("# 06 DOCUMENT SUMMARIES\n\n")
    for d in data:
        f.write(f"## {clean_id(d['doc_id'])}: {d['title']}\n\n")
        f.write(f"- **Purpose:** {d['purpose']}\n")
        f.write(f"- **File Path:** {d['file_path']}\n")
        f.write(f"- **Dependencies:** {', '.join(d['depends_on'])}\n")
        f.write(f"- **Status:** {d['status']} ({d['version']})\n\n")

# 05_CONCEPT_INDEX.md
with open('Constitutional Reviews/Discovery/05_CONCEPT_INDEX.md', 'w') as f:
    f.write("# 05 CONCEPT INDEX\n\n")
    f.write("| Concept | Primary Defining Document | Definition |\n")
    f.write("| --- | --- | --- |\n")
    sorted_concepts = sorted(concepts.items())
    for concept, cdata in sorted_concepts:
        f.write(f"| {concept} | {cdata['owning_document']} | {cdata['definition']} |\n")
