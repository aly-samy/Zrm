import json
import os

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

with open('Constitutional Reviews/Discovery/09_REPOSITORY_REORGANIZATION_PLAN.md', 'w') as f:
    f.write("# 09 REPOSITORY REORGANIZATION PLAN\n\n")
    f.write("| Current File | Proposed /ZRMv3/ Path | Proposed Filename | Action | Reason |\n")
    f.write("| --- | --- | --- | --- | --- |\n")

    for d in data:
        cur = d['file_path']
        score = d['authority_score']
        did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')

        # New path logic
        folder = "10_Archive"
        if score == "Foundation": folder = "01_Foundation"
        elif score == "Constitutional": folder = "02_Constitution"
        elif score == "Capability": folder = "03_Capabilities"
        elif score == "Runtime": folder = "04_Runtime"
        elif score == "Supporting": folder = "05_Supporting"
        elif score == "Historical": folder = "09_Historical"

        new_name = f"{did}.md"
        if did == "Unknown": new_name = cur.split('/')[-1]

        action = "Move"
        if score in ["Foundation", "Constitutional"]: action = "Promote"
        if score == "Archive": action = "Archive"

        f.write(f"| {cur} | /ZRMv3/{folder}/ | {new_name} | {action} | Authority: {score} |\n")
