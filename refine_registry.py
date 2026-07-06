import json
import re

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

for d in data:
    did = d['doc_id']
    title = d['title']
    fp = d['file_path']

    # Heuristic for ID from Title if ID is Unknown
    if did == "Unknown":
        if "NORTH STAR" in title.upper(): did = "NORTH-STAR"
        elif "FOUNDING PRINCIPLE" in title.upper(): did = "FOUNDING-PRINCIPLES"
        elif "PRD" in title.upper(): did = "PRD"
        elif "ROADMAP" in title.upper(): did = "ROADMAP"
        elif "ZRM V1.1" in title.upper(): did = "ZRM-V1.1"
        elif "STATE OF THE UNION" in title.upper(): did = "STATE-OF-THE-UNION"
        elif "DATA MODEL" in title.upper(): did = "DATA-MODEL"
        elif "TECH-ARCHITECTURE" in fp.upper(): did = "TECH-ARCH"

    # Extract version from title if unknown
    if d['version'] == "Unknown":
        v_match = re.search(r'v(\d+\.\d+)', title, re.IGNORECASE)
        if v_match: d['version'] = v_match.group(1)

    d['doc_id'] = did

with open('deep_analysis.json', 'w') as f:
    json.dump(data, f, indent=2)
