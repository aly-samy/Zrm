with open('Constitutional Reviews/Discovery/13_MIGRATION_ORDER.md', 'w') as f:
    f.write("# 13 MIGRATION ORDER\n\n")
    f.write("## Phase 1: Foundation (Authority Tier 0)\n")
    f.write("- Move North Star, Founding Principles, and State of the Union.\n")
    f.write("- Verify baseline integrity.\n\n")
    f.write("## Phase 2: Core Constitution (Authority Tier 1)\n")
    f.write("- Move ZRM series, CMP, and SR-001.\n")
    f.write("- Update references between Foundation and Constitution.\n\n")
    f.write("## Phase 3: Capability Layer (Authority Tier 2)\n")
    f.write("- Move WS (Specifications) and RI (Reference Implementations) series.\n")
    f.write("- Consolidate duplicate blueprints.\n\n")
    f.write("## Phase 4: Runtime & Supporting (Authority Tier 3)\n")
    f.write("- Move SDK, Platform Spec, and Developer Journeys.\n")
    f.write("- Archive legacy drafts and roundtable notes.\n\n")
    f.write("## Phase 5: Verification & Cleanup\n")
    f.write("- Final link validation.\n")
    f.write("- Remove original legacy directories.\n")

# Report 14: RENAME_MAP.md
import json
with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

with open('Constitutional Reviews/Discovery/14_RENAME_MAP.md', 'w') as f:
    f.write("# 14 RENAME MAP\n\n")
    f.write("| Old Filename | New Filename |\n")
    f.write("| --- | --- |\n")
    for d in data:
        cur = d['file_path']
        score = d['authority_score']
        did = d['doc_id'].split('**')[0].strip().replace('Document ID: ', '').replace(' ', '_')
        folder = "10_Archive"
        if score == "Foundation": folder = "01_Foundation"
        elif score == "Constitutional": folder = "02_Constitution"
        elif score == "Capability": folder = "03_Capabilities"
        elif score == "Runtime": folder = "04_Runtime"
        elif score == "Supporting": folder = "05_Supporting"
        elif score == "Historical": folder = "09_Historical"

        new_name = f"{did}.md"
        if did == "Unknown": new_name = cur.split('/')[-1]

        f.write(f"| {cur} | /ZRMv3/{folder}/{new_name} |\n")

# Report 16: ARCHIVE_CANDIDATES.md
with open('Constitutional Reviews/Discovery/16_ARCHIVE_CANDIDATES.md', 'w') as f:
    f.write("# 16 ARCHIVE CANDIDATES\n\n")
    f.write("Documents excluded from /ZRMv3/ core due to authority score 'Archive' or 'Historical'.\n\n")
    for d in data:
        if d['authority_score'] in ["Archive", "Historical"]:
            f.write(f"- **{d['doc_id']}**: {d['title']} ({d['file_path']})\n")
