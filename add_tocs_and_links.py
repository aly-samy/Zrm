import os

reports = [
    "00_MISSION_EXECUTIVE_SUMMARY.md",
    "01_DOCUMENT_REGISTRY.md",
    "02_CONSTITUTIONAL_HIERARCHY.md",
    "03_DEPENDENCY_GRAPH.md",
    "04_CITATION_INDEX.md",
    "05_CONCEPT_INDEX.md",
    "06_DOCUMENT_SUMMARIES.md",
    "07_KNOWLEDGE_GRAPH.md",
    "08_DISCOVERY_FINDINGS.md",
    "09_REPOSITORY_REORGANIZATION_PLAN.md",
    "10_CANONICAL_DOCUMENT_REGISTRY.md",
    "11_FILE_CONSOLIDATION_REPORT.md",
    "12_PROPOSED_DIRECTORY_TREE.md",
    "13_MIGRATION_ORDER.md",
    "14_RENAME_MAP.md",
    "15_LINK_UPDATE_PLAN.md",
    "16_ARCHIVE_CANDIDATES.md"
]

base_dir = "Constitutional Reviews/Discovery/"

for report in reports:
    path = os.path.join(base_dir, report)
    if not os.path.exists(path): continue

    with open(path, 'r') as f:
        content = f.read()

    related = "## Related Reports\n\n"
    for r in reports:
        if r != report:
            related += f"- [{r.replace('_', ' ').replace('.md', '')}]({r})\n"

    toc = ""
    if report in ["01_DOCUMENT_REGISTRY.md", "05_CONCEPT_INDEX.md", "06_DOCUMENT_SUMMARIES.md", "09_REPOSITORY_REORGANIZATION_PLAN.md", "14_RENAME_MAP.md", "15_LINK_UPDATE_PLAN.md"]:
        toc = "## Table of Contents\n\n"
        # Only grab top headers
        headers = [line.strip('# ').strip() for line in content.split('\n') if line.startswith('## ')]
        for h in headers:
            anchor = h.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('/', '')
            toc += f"- [{h}](#{anchor})\n"
        toc += "\n---\n\n"

    new_content = content.split('\n')[0] + "\n\n" + toc + "\n".join(content.split('\n')[1:]) + "\n\n" + related

    with open(path, 'w') as f:
        f.write(new_content)
