import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# Build map of ID -> New Path
id_to_new = {}
for d in data:
    did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')
    score = d['authority_score']
    folder = "10_Archive"
    if score == "Foundation": folder = "01_Foundation"
    elif score == "Constitutional": folder = "02_Constitution"
    elif score == "Capability": folder = "03_Capabilities"
    elif score == "Runtime": folder = "04_Runtime"
    elif score == "Supporting": folder = "05_Supporting"
    elif score == "Historical": folder = "09_Historical"

    new_name = f"{did}.md"
    if did == "Unknown": new_name = d['file_path'].split('/')[-1]
    id_to_new[did.upper()] = f"/ZRMv3/{folder}/{new_name}"

with open('Constitutional Reviews/Discovery/15_LINK_UPDATE_PLAN.md', 'w') as f:
    f.write("# 15 LINK UPDATE PLAN\n\n")
    f.write("| Document | Broken Reference | Proposed Replacement | Confidence |\n")
    f.write("| --- | --- | --- | --- |\n")

    for d in data:
        source = d['doc_id']
        for ref in d['doc_refs']:
            ref_up = ref.upper()
            if ref_up in id_to_new:
                f.write(f"| {source} | {ref} | {id_to_new[ref_up]} | High |\n")
            else:
                f.write(f"| {source} | {ref} | UNRESOLVED | Low |\n")
