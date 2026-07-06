import json
import os

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

for d in data:
    did = d['doc_id'].upper()
    fp = d['file_path'].upper()
    title = d['title'].upper()

    score = "Archive" # Default

    # Foundation
    if "NORTH-STAR" in did or "FOUNDING" in did or "NORTH-STAR" in title or "FOUNDING" in title:
        score = "Foundation"
    # Constitutional
    elif any(x in did for x in ["ZRM-000", "ZRM-001", "ZRM-002", "CMP", "SR-001", "CFR-001"]):
        score = "Constitutional"
    # Capability
    elif any(x in did for x in ["WS-", "RI-", "RSN-", "ARM-", "PRJ-", "EXP-", "ZT-", "RSN-"]):
        score = "Capability"
    # Runtime
    elif "SDK" in did or "SDK" in title or "PLATFORM-SPEC" in did or "API" in title:
        score = "Runtime"
    # Supporting
    elif any(x in did for x in ["DJ-", "PRD", "ROADMAP", "DATA-MODEL", "TECH-ARCH", "STATE-OF-THE-UNION"]):
        score = "Supporting"
    # Historical / Archive detection
    if "V1" in title or "V1" in fp or "DRAFT" in d['status'].upper() or "RTC" in fp or "REVISION" in title:
        # If it was something high but is an old version, it's historical
        if score in ["Foundation", "Constitutional", "Capability", "Runtime"]:
             score = "Historical"
        else:
             score = "Archive"

    # Specific overrides based on path
    if "/RATIFIED/" in fp and score not in ["Foundation", "Constitutional"]:
        if score == "Archive": score = "Supporting"

    if "RTC" in fp: score = "Archive"

    d['authority_score'] = score

with open('deep_analysis.json', 'w') as f:
    json.dump(data, f, indent=2)
