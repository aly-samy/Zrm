import os
import re
import json

files_list = "constitutional_candidates.txt"
with open(files_list, 'r') as f:
    files = [line.strip() for line in f if line.strip()]

concepts = {}

# Broaden definition patterns
def_patterns = [
    r'^\s*\*\s*\*\*([A-Z][A-Z\s]+)\*\*\s*[:\-]\s*(.+)', # * **TERM** - Definition
    r'^\s*\d+\.\s+\*\*([A-Z][a-z]+)\*\*\s*[:\-]\s*(.+)', # 1. **Term** - Definition
    r'^\*\*([A-Z][A-Z\s]+)\*\*\s*[:\-]\s*(.+)', # **TERM** - Definition
    r'^###\s+([A-Z][a-z]+)\s*\n\s*(.+)', # ### Term \n Definition
]

for file_path in files:
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    for pattern in def_patterns:
        matches = re.finditer(pattern, content, re.MULTILINE)
        for match in matches:
            term = match.group(1).strip().upper()
            definition = match.group(2).strip()
            if term not in concepts:
                concepts[term] = {
                    "definition": definition,
                    "owning_document": file_path,
                    "references": []
                }
            else:
                if file_path not in concepts[term]["references"]:
                    concepts[term]["references"].append(file_path)

with open('raw_concepts.json', 'w') as f:
    json.dump(concepts, f, indent=2)
