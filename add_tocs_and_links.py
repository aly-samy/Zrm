import os

reports = [
    "01_DOCUMENT_REGISTRY.md",
    "02_CONSTITUTIONAL_HIERARCHY.md",
    "03_DEPENDENCY_GRAPH.md",
    "04_CITATION_INDEX.md",
    "05_CONCEPT_INDEX.md",
    "06_DOCUMENT_SUMMARIES.md",
    "07_KNOWLEDGE_GRAPH.md",
    "08_DISCOVERY_FINDINGS.md",
    "09_DISCOVERY_EXECUTIVE_SUMMARY.md"
]

base_dir = "Constitutional Reviews/Discovery/"

for report in reports:
    path = os.path.join(base_dir, report)
    if not os.path.exists(path): continue

    with open(path, 'r') as f:
        content = f.read()

    # Add Related Reports section at the end
    related = "## Related Reports\n\n"
    for r in reports:
        if r != report:
            related += f"- [{r.replace('_', ' ').replace('.md', '')}]({r})\n"

    # Add TOC for long reports
    toc = ""
    if report in ["01_DOCUMENT_REGISTRY.md", "05_CONCEPT_INDEX.md", "06_DOCUMENT_SUMMARIES.md"]:
        toc = "## Table of Contents\n\n"
        headers = [line.strip('# ').strip() for line in content.split('\n') if line.startswith('## ')]
        for h in headers:
            anchor = h.lower().replace(' ', '-').replace(':', '').replace('.', '')
            toc += f"- [{h}](#{anchor})\n"
        toc += "\n---\n\n"

    new_content = content.split('\n')[0] + "\n\n" + toc + "\n".join(content.split('\n')[1:]) + "\n\n" + related

    with open(path, 'w') as f:
        f.write(new_content)
