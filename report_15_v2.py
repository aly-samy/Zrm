import json

with open('intelligence_results.json', 'r') as f:
    intel = json.load(f)

with open('Constitutional Reviews/Discovery/15_GAP_ANALYSIS.md', 'w') as f:
    f.write("# 15 GAP ANALYSIS\n\n")
    f.write("Identified missing constitutional documents or structural gaps.\n\n")
    f.write("| Source Document | Referenced Target | Status |\n")
    f.write("| --- | --- | --- |\n")
    for gap in intel['gaps']:
        f.write(f"| {gap['source']} | {gap['target']} | MISSING |\n")
