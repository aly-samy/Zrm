import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

# Detect duplicates by title
titles = {}
for d in data:
    t = d['title'].upper()
    if t not in titles: titles[t] = []
    titles[t].append(d)

with open('Constitutional Reviews/Discovery/11_DUPLICATE_AND_SUPERSESSION_ANALYSIS.md', 'w') as f:
    f.write("# 11 DUPLICATE AND SUPERSESSION ANALYSIS\n\n")
    for title, docs in titles.items():
        if len(docs) > 1 and title != "UNKNOWN":
            f.write(f"### Entity: {title}\n")
            # Heuristic for latest: ratified path or version number
            latest = docs[0]
            for doc in docs:
                if "/ratified/" in doc['file_path'].lower():
                    latest = doc

            f.write(f"- **Latest/Authoritative:** {latest['file_path']}\n")
            f.write("- **Superseded/Archive:**\n")
            for doc in docs:
                if doc != latest:
                    f.write(f"  - {doc['file_path']}\n")
            f.write("\n")
