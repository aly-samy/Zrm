import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# Group by logical ID
entities = {}
for d in data:
    did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')
    if did not in entities:
        entities[did] = []
    entities[did].append(d)

with open('Constitutional Reviews/Discovery/10_CANONICAL_DOCUMENT_REGISTRY.md', 'w') as f:
    f.write("# 10 CANONICAL DOCUMENT REGISTRY\n\n")
    for eid, files in entities.items():
        if eid == "Unknown": continue
        active = files[0] # Simplification
        f.write(f"### {eid}\n")
        f.write(f"- **Current file:** {active['file_path']}\n")
        f.write(f"- **Status:** {active['status']}\n")
        f.write(f"- **Depends on:** {', '.join(active['depends_on'])}\n")
        f.write(f"- **Authority Score:** {active['authority_score']}\n")
        f.write(f"- **Files in Group:** {len(files)}\n")
        f.write("\n")
