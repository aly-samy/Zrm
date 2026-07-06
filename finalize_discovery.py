import json

with open('raw_metadata.json', 'r') as f:
    metadata = json.load(f)

with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

with open('raw_summaries.json', 'r') as f:
    summaries = json.load(f)

# Cross-reference for Referenced By
id_to_file = {m["doc_id"]: m["file_path"] for m in metadata if m["doc_id"] != "Unknown"}

for entry in metadata:
    for ref in entry["references"]:
        # Find who refers to this
        target_summary = next((s for s in summaries if s["doc_id"] == ref), None)
        if target_summary:
            if entry["doc_id"] not in target_summary["referenced_by"]:
                target_summary["referenced_by"].append(entry["doc_id"])

# Write Report 01: DOCUMENT_REGISTRY.md
with open('Constitutional Reviews/Discovery/01_DOCUMENT_REGISTRY.md', 'w') as f:
    f.write("# 01 DOCUMENT REGISTRY\n\n")
    f.write("| Document ID | Title | Version | Status | File Path | Author |\n")
    f.write("| --- | --- | --- | --- | --- | --- |\n")
    for m in metadata:
        f.write(f"| {m['doc_id']} | {m['title']} | {m['version']} | {m['status']} | {m['file_path']} | {m['author']} |\n")

# Write Report 06: DOCUMENT_SUMMARIES.md
with open('Constitutional Reviews/Discovery/06_DOCUMENT_SUMMARIES.md', 'w') as f:
    f.write("# 06 DOCUMENT SUMMARIES\n\n")
    for s in summaries:
        f.write(f"## {s['doc_id']}: {s['title']}\n\n")
        f.write(f"- **File Path:** {s['file_path']}\n")
        f.write(f"- **Purpose:** {s['purpose']}\n")
        f.write(f"- **Dependencies:** {', '.join(s['dependencies'])}\n")
        f.write(f"- **Referenced By:** {', '.join(s['referenced_by'])}\n\n")

# Write Report 05: CONCEPT_INDEX.md
with open('Constitutional Reviews/Discovery/05_CONCEPT_INDEX.md', 'w') as f:
    f.write("# 05 CONCEPT INDEX\n\n")
    f.write("| Concept | Primary Defining Document | Definition |\n")
    f.write("| --- | --- | --- |\n")
    for concept, data in concepts.items():
        f.write(f"| {concept} | {data['owning_document']} | {data['definition']} |\n")
