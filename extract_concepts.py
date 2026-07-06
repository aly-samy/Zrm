import os
import re
import json

files_list = "constitutional_candidates.txt"
with open(files_list, 'r') as f:
    files = [line.strip() for line in f if line.strip()]

concepts = {}

# Patterns for definitions (e.g., "Term: Definition" or "### Term\nDefinition")
def_patterns = [
    r'^\*\*([A-Z][a-z]+)\*\*:\s+(.+)',
    r'^###\s+([A-Z][a-z]+)\s*\n\s*(.+)',
    r'^\*([A-Z][a-z]+)\*:\s+(.+)'
]

for file_path in files:
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        for pattern in def_patterns:
            match = re.search(pattern, line)
            if match:
                term = match.group(1).strip()
                definition = match.group(2).strip()
                if term not in concepts:
                    concepts[term] = {
                        "definition": definition,
                        "owning_document": file_path,
                        "references": []
                    }
                else:
                    concepts[term]["references"].append(file_path)

with open('raw_concepts.json', 'w') as f:
    json.dump(concepts, f, indent=2)
