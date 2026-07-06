import os
import re
import json

with open('raw_metadata.json', 'r') as f:
    metadata = json.load(f)

summaries = []

for entry in metadata:
    file_path = entry["file_path"]
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Heuristic for purpose: first paragraph after title
    purpose = "Unknown"
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('#'):
            for next_line in lines[i+1:]:
                if next_line.strip() and not next_line.startswith('#'):
                    purpose = next_line.strip()[:300] + "..."
                    break
            break

    summary = {
        "doc_id": entry["doc_id"],
        "title": entry["title"],
        "file_path": file_path,
        "purpose": purpose,
        "scope": "Unknown",
        "major_concepts": [],
        "responsibilities": "Unknown",
        "dependencies": entry["depends_on"],
        "referenced_by": [] # To be filled by cross-ref
    }
    summaries.append(summary)

with open('raw_summaries.json', 'w') as f:
    json.dump(summaries, f, indent=2)
