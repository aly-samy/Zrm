import json

with open('intelligence_results.json', 'r') as f:
    intel = json.load(f)

with open('Constitutional Reviews/Discovery/14_CONFLICT_ANALYSIS.md', 'w') as f:
    f.write("# 14 CONFLICT ANALYSIS\n\n")
    f.write("Concepts defined in multiple documents potentially creating semantic ambiguity.\n\n")
    for concept, docs in intel['conflicts'].items():
        if len(docs) > 1:
            f.write(f"### {concept}\n")
            f.write("Defined in:\n")
            for d in set(docs):
                f.write(f"- {d}\n")
            f.write("\n")
