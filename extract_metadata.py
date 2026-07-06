import os
import re
import json

files_list = "constitutional_candidates.txt"
with open(files_list, 'r') as f:
    files = [line.strip() for line in f if line.strip()]

results = []

for file_path in files:
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    metadata = {
        "file_path": file_path,
        "doc_id": "Unknown",
        "title": "Unknown",
        "version": "Unknown",
        "status": "Unknown",
        "lifecycle": "Unknown",
        "author": "Unknown",
        "date": "Unknown",
        "depends_on": [],
        "supersedes": [],
        "superseded_by": [],
        "parent": "Unknown",
        "children": [],
        "references": []
    }

    # Try to find Title in first few lines (H1)
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match:
        metadata["title"] = title_match.group(1).strip()

    # Extract common fields
    id_match = re.search(r'(?:Document ID|ID):\s*([\w\-\.\(\) ]+)', content, re.IGNORECASE)
    if id_match:
        metadata["doc_id"] = id_match.group(1).strip()

    ver_match = re.search(r'Version:\s*([\w\.\-]+)', content, re.IGNORECASE)
    if ver_match:
        metadata["version"] = ver_match.group(1).strip()

    status_match = re.search(r'Status:\s*([\w\s\-]+)', content, re.IGNORECASE)
    if status_match:
        metadata["status"] = status_match.group(1).strip().split('\n')[0].split('**')[0].strip()

    author_match = re.search(r'(?:Author|By):\s*([\w\s\. ]+)', content, re.IGNORECASE)
    if author_match:
        metadata["author"] = author_match.group(1).strip().split('\n')[0].strip()

    date_match = re.search(r'Date:\s*([\w\s\d,]+)', content, re.IGNORECASE)
    if date_match:
        metadata["date"] = date_match.group(1).strip().split('\n')[0].strip()

    # Dependencies and References
    depends_match = re.search(r'Depends On:\s*([^\n]+)', content, re.IGNORECASE)
    if depends_match:
        deps = re.split(r'[,\s·]+', depends_match.group(1))
        metadata["depends_on"] = [d.strip() for d in deps if d.strip()]

    # References (search for IDs like WS-001, RI-001, etc.)
    ref_matches = re.findall(r'([A-Z]{2,4}-\d{3}[A-Z\d\.]*)', content)
    metadata["references"] = list(set(ref_matches))

    results.append(metadata)

with open('raw_metadata.json', 'w') as f:
    json.dump(results, f, indent=2)
