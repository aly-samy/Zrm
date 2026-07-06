import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

with open('Constitutional Reviews/Discovery/16_AI_NAVIGATION_INDEX.md', 'w') as f:
    f.write("# 16 AI NAVIGATION INDEX\n\n")
    for d in data:
        f.write(f"### {d['doc_id']}\n")
        f.write(f"- **Summary:** {d['purpose']}\n")
        f.write(f"- **Depends on:** {', '.join(d['depends_on'])}\n")
        f.write(f"- **Refers to:** {', '.join(d['doc_refs'][:10])}\n")
        f.write(f"- **Defines:** {', '.join(d.get('defines', []))}\n")
        f.write("\n")
