import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

tree = {
    "00_READ_FIRST": ["README.md"],
    "01_Foundation": [],
    "02_Constitution": [],
    "03_Capabilities": [],
    "04_Runtime": [],
    "05_Supporting": [],
    "09_Historical": [],
    "10_Archive": []
}

for d in data:
    score = d['authority_score']
    did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')
    new_name = f"{did}.md"
    if did == "Unknown": new_name = d['file_path'].split('/')[-1]

    if score == "Foundation": tree["01_Foundation"].append(new_name)
    elif score == "Constitutional": tree["02_Constitution"].append(new_name)
    elif score == "Capability": tree["03_Capabilities"].append(new_name)
    elif score == "Runtime": tree["04_Runtime"].append(new_name)
    elif score == "Supporting": tree["05_Supporting"].append(new_name)
    elif score == "Historical": tree["09_Historical"].append(new_name)
    else: tree["10_Archive"].append(new_name)

with open('Constitutional Reviews/Discovery/12_PROPOSED_DIRECTORY_TREE.md', 'w') as f:
    f.write("# 12 PROPOSED DIRECTORY TREE\n\n")
    f.write("## /ZRMv3/\n")
    for folder, files in sorted(tree.items()):
        f.write(f"- **{folder}/**\n")
        for file in sorted(set(files)):
            f.write(f"  - {file}\n")
