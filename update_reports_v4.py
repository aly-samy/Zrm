import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# Helper to clean Doc IDs
def clean_id(did):
    return did.split('**')[0].strip().replace('Document ID: ', '')

# 01_DOCUMENT_REGISTRY.md
with open('Constitutional Reviews/Discovery/01_DOCUMENT_REGISTRY.md', 'w') as f:
    f.write("# 01 DOCUMENT REGISTRY\n\n")
    f.write("| ID | Title | Authority Score | Status | Path |\n")
    f.write("| --- | --- | --- | --- | --- |\n")
    for d in data:
        f.write(f"| {clean_id(d['doc_id'])} | {d['title']} | {d['authority_score']} | {d['status']} | {d['file_path']} |\n")

# 05_CONCEPT_INDEX.md
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

with open('Constitutional Reviews/Discovery/05_CONCEPT_INDEX.md', 'w') as f:
    f.write("# 05 CONCEPT INDEX\n\n")
    f.write("| Concept | Owner | Authority Score | Definition |\n")
    f.write("| --- | --- | --- | --- |\n")
    for c, cdata in sorted(concepts.items()):
        # Find score for owner
        score = "Unknown"
        for d in data:
            if d['file_path'] == cdata['owning_document']:
                score = d['authority_score']
                break
        f.write(f"| {c} | {cdata['owning_document']} | {score} | {cdata['definition']} |\n")
