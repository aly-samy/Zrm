import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

with open('Constitutional Reviews/Discovery/10_MIGRATION_PLAN.md', 'w') as f:
    f.write("# 10 MIGRATION PLAN\n\n")
    f.write("| Old Path | New Path | Action | Reason |\n")
    f.write("| --- | --- | --- | --- |\n")
    for d in data:
        old = d['file_path']
        score = d['authority_score']
        did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')

        folder = "10-Archive"
        if score == "Foundation": folder = "01-Foundations"
        elif score == "Constitutional": folder = "02-Constitution"
        elif score == "Capability": folder = "03-World-Specifications"
        elif score == "Runtime": folder = "05-Runtime"
        elif score == "Supporting": folder = "09-Reference"

        new = f"/ZRMv3/{folder}/{did}.md"
        if did == "Unknown": new = f"/ZRMv3/{folder}/{old.split('/')[-1]}"

        action = "Move"
        if score == "Archive": action = "Archive"
        elif score == "Historical": action = "Archive"

        f.write(f"| {old} | {new} | {action} | Tier: {score} |\n")
