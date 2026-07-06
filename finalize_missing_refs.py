import json
import os

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# All known Doc IDs
known_ids = set()
for d in data:
    did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '')
    if did != "Unknown":
        known_ids.add(did.upper())

missing_refs = []

# Check all references in all documents
for d in data:
    source = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '')
    for ref in d['doc_refs']:
        ref_up = ref.upper()
        if ref_up not in known_ids and not any(ext in ref_up for ext in ['.MD', '.JPG', '.PNG', '.PDF']):
            # Filter out some false positives like RFCs if they are external
            if not ref_up.startswith('RFC-') and not ref_up.startswith('ISO-'):
                 missing_refs.append({
                     "source": source,
                     "target": ref,
                     "file": d['file_path']
                 })

# Update Report 08 with explicit missing refs list
with open('Constitutional Reviews/Discovery/08_DISCOVERY_FINDINGS.md', 'a') as f:
    f.write("\n## 3. Missing Dependencies & Unresolved References\n")
    f.write("| Source Document | Missing Target | File Path |\n")
    f.write("| --- | --- | --- |\n")
    for m in missing_refs[:50]: # Cap it for the report
        f.write(f"| {m['source']} | {m['target']} | {m['file']} |\n")
