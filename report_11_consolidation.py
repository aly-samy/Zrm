import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# Detect duplicates by title
titles = {}
for d in data:
    t = d['title'].upper()
    if t not in titles: titles[t] = []
    titles[t].append(d)

with open('Constitutional Reviews/Discovery/11_FILE_CONSOLIDATION_REPORT.md', 'w') as f:
    f.write("# 11 FILE CONSOLIDATION REPORT\n\n")
    for title, docs in titles.items():
        if len(docs) > 1 and title != "UNKNOWN":
            f.write(f"### Duplicate Group: {title}\n")
            # Prefer ratified/ over others
            keep = docs[0]
            for doc in docs:
                if "/ratified/" in doc['file_path'].lower():
                    keep = doc

            f.write(f"- **Keep:** {keep['file_path']}\n")
            f.write("- **Archive:**\n")
            for doc in docs:
                if doc != keep:
                    f.write(f"  - {doc['file_path']}\n")
            f.write("\n")
