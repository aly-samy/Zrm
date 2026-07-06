import os
import re
import json

def extract_sections(content):
    # Matches patterns like "Section 1", "§ 1.1", "Part 2"
    sections = re.findall(r'(?:Section|§|Part)\s*(\d+[\.\w]*)', content, re.IGNORECASE)
    return list(set(sections))

def find_citations(content):
    # Matches document IDs like WS-001, RI-001, etc. and sections like §5
    citations = re.findall(r'([A-Z]{2,5}-\d{3}[A-Z\d\.]*|§\s*\d+[\.\w]*)', content)
    return list(set(citations))

with open('constitutional_candidates.txt', 'r') as f:
    files = [line.strip() for line in f if line.strip()]

all_data = []

for file_path in files:
    if not os.path.exists(file_path): continue
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Metadata extraction
    doc_id = "Unknown"
    id_match = re.search(r'(?:Document ID|ID):\s*([\w\-\.\(\) ]+)', content, re.IGNORECASE)
    if id_match: doc_id = id_match.group(1).strip()

    title = "Unknown"
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match: title = title_match.group(1).strip()

    # Refs and Sections
    raw_citations = find_citations(content)
    doc_refs = [c for c in raw_citations if '-' in c]
    section_refs = [c for c in raw_citations if '§' in c]

    # Summaries (refined)
    summary_purpose = "Unknown"
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('#'):
            for next_line in lines[i+1:]:
                if next_line.strip() and not next_line.startswith('#'):
                    summary_purpose = next_line.strip()[:500]
                    break
            break

    all_data.append({
        "file_path": file_path,
        "doc_id": doc_id,
        "title": title,
        "version": "Unknown", # Extracted in next pass if needed
        "status": "Unknown",
        "lifecycle": "Unknown",
        "author": "Unknown",
        "date": "Unknown",
        "depends_on": [],
        "doc_refs": doc_refs,
        "section_refs": section_refs,
        "purpose": summary_purpose,
        "content": content[:2000] # for light analysis
    })

# Secondary pass for common metadata
for entry in all_data:
    content = entry["content"]
    ver_match = re.search(r'Version:\s*([\w\.\-]+)', content, re.IGNORECASE)
    if ver_match: entry["version"] = ver_match.group(1).strip()

    status_match = re.search(r'Status:\s*([\w\s\-]+)', content, re.IGNORECASE)
    if status_match: entry["status"] = status_match.group(1).strip().split('\n')[0].split('**')[0].strip()

    author_match = re.search(r'(?:Author|By):\s*([\w\s\. ]+)', content, re.IGNORECASE)
    if author_match: entry["author"] = author_match.group(1).strip().split('\n')[0].strip()

    date_match = re.search(r'Date:\s*([\w\s\d,]+)', content, re.IGNORECASE)
    if date_match: entry["date"] = date_match.group(1).strip().split('\n')[0].strip()

    depends_match = re.search(r'Depends On:\s*([^\n]+)', content, re.IGNORECASE)
    if depends_match:
        deps = re.split(r'[,\s·]+', depends_match.group(1))
        entry["depends_on"] = [d.strip() for d in deps if d.strip() and d.strip() != 'None']

with open('deep_analysis.json', 'w') as f:
    json.dump(all_data, f, indent=2)
