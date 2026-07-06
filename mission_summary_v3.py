import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

doc_count = len(data)

with open('Constitutional Reviews/Discovery/00_MISSION_EXECUTIVE_SUMMARY.md', 'w') as f:
    f.write("# 00 MISSION EXECUTIVE SUMMARY\n\n")
    f.write("## 1. Discovery & Intelligence Overview\n")
    f.write(f"- **Total Constitutional Artifacts Mapped:** {doc_count}\n")
    f.write("- **Primary File Families:** ZRM, WS, RI, RSN, SDK, DJ, CA, RTC\n")
    f.write("- **Canonical Authority Analysis:** All documents tiered into Foundations, Constitution, Capabilities, Runtime, Supporting, and Archive.\n\n")

    f.write("## 2. Migration Assessment Summary\n")
    f.write("- **Directory Restructure:** Proposed ideal ZRMv3 layout (Report 09).\n")
    f.write("- **Migration Plan:** Detailed file-by-file execution checklist (Report 10).\n")
    f.write("- **Health Score:** Repository integrity evaluated at Tier 2 (Average 6/10), requiring systematic cleanup (Report 17).\n\n")

    f.write("## 3. Key Findings\n")
    f.write("- **Semantic Debt:** Multiple conflicting definitions for core concepts (Identity, Reality) found across layers (Report 14).\n")
    f.write("- **Knowledge Gaps:** Critical missing dependencies identified for FED and Marketplace specifications (Report 15).\n")
    f.write("- **Orphan Proliferation:** Significant volume of disconnected artifacts discovered in RTC (Roundtable) and legacy folders (Report 13).\n")
