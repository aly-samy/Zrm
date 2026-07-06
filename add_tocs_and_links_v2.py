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
    "09_DIRECTORY_RESTRUCTURE_PROPOSAL.md",
    "10_MIGRATION_PLAN.md",
    "11_DUPLICATE_AND_SUPERSESSION_ANALYSIS.md",
    "12_CANONICAL_NAMING_STANDARD.md",
    "13_ORPHAN_ANALYSIS.md",
    "14_CONFLICT_ANALYSIS.md",
    "15_GAP_ANALYSIS.md",
    "16_AI_NAVIGATION_INDEX.md",
    "17_REPOSITORY_HEALTH_SCORE.md"
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
    # Add TOC for long reports
    if report in ["01_DOCUMENT_REGISTRY.md", "06_DOCUMENT_SUMMARIES.md", "10_MIGRATION_PLAN.md", "16_AI_NAVIGATION_INDEX.md"]:
        toc = "## Table of Contents\n\n"
        lines = content.split('\n')
        for line in lines:
            if line.startswith('## ') or line.startswith('### '):
                h = line.strip('# ').strip()
                anchor = h.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('/', '')
                indent = "  " if line.startswith('### ') else ""
                toc += f"{indent}- [{h}](#{anchor})\n"
        toc += "\n---\n\n"

    new_content = content.split('\n')[0] + "\n\n" + toc + "\n".join(content.split('\n')[1:]) + "\n\n" + related

    with open(path, 'w') as f:
        f.write(new_content)
