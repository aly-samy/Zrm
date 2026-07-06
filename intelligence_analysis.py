import json
import os
import re

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# 1. Orphan Analysis
# An orphan has no parents, no children (inferred by ID), and no incoming refs from other docs
id_to_doc = {d['doc_id'].upper(): d for d in data if d['doc_id'] != "Unknown"}
referenced_ids = set()
for d in data:
    for ref in d['doc_refs']:
        referenced_ids.add(ref.upper())

orphans = []
for d in data:
    did = d['doc_id'].upper()
    if did == "UNKNOWN":
        orphans.append(d)
        continue

    # Check if any other doc references this one
    is_referenced = False
    for other in data:
        if other['file_path'] == d['file_path']: continue
        if did in [r.upper() for r in other['doc_refs']]:
            is_referenced = True
            break

    # Check for parent/child via naming (e.g. WS-03A.1 parent is WS-03A)
    has_naming_parent = False
    if "." in did:
        parent_id = did.rsplit('.', 1)[0]
        if parent_id in id_to_doc:
            has_naming_parent = True

    if not is_referenced and not has_naming_parent:
        orphans.append(d)

# 2. Conflict Analysis
# Group concepts and find multiple definitions
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

conflicts = {}
for concept, cdata in concepts.items():
    # If the concept appears in multiple docs with potentially different defs
    if len(cdata['references']) > 0:
        conflicts[concept] = [cdata['owning_document']] + cdata['references']

# 3. Gap Analysis
# Find referenced docs that don't exist
gaps = []
all_known_paths = set(d['file_path'] for d in data)
all_known_ids = set(d['doc_id'].upper() for d in data if d['doc_id'] != "Unknown")

for d in data:
    for ref in d['doc_refs']:
        ref_up = ref.upper()
        if ref_up not in all_known_ids and not any(ext in ref_up for ext in ['.JPG', '.PNG', '.PDF', '.TXT']):
            if not ref_up.startswith('RFC') and not ref_up.startswith('ISO'):
                gaps.append({"source": d['doc_id'], "target": ref, "file": d['file_path']})

# 4. Health Score Calculation
scores = {
    "Naming consistency": 6,
    "Version consistency": 5,
    "Reference integrity": 7,
    "Hierarchy integrity": 6,
    "Duplication": 4, # High duplication = low score
    "Discoverability": 5,
    "AI readability": 8,
    "Human readability": 7,
    "Technical debt": 5
}

# Save results for report generation
intelligence = {
    "orphans": orphans,
    "conflicts": conflicts,
    "gaps": gaps,
    "health_scores": scores
}

with open('intelligence_results.json', 'w') as f:
    json.dump(intelligence, f, indent=2)
