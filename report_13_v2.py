import json

with open('intelligence_results.json', 'r') as f:
    intel = json.load(f)

with open('Constitutional Reviews/Discovery/13_ORPHAN_ANALYSIS.md', 'w') as f:
    f.write("# 13 ORPHAN ANALYSIS\n\n")
    f.write("Documents with no incoming references, parent relationships, or children.\n\n")
    f.write("| ID | File Path | Authority Score |\n")
    f.write("| --- | --- | --- |\n")
    for o in intel['orphans']:
        f.write(f"| {o['doc_id']} | {o['file_path']} | {o['authority_score']} |\n")
