import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)

hierarchy = {
    "Foundational": [], # NORTH-STAR, FOUNDING-PRINCIPLES
    "ZRM (Reality Model)": [], # ZRM Series
    "WS (Specifications)": [], # WS Series
    "RI (Reference Implementations)": [], # RI Series
    "RSN (Reasoning)": [], # RSN Series
    "Governance/Amendments": [], # CA, CMP, SR, CRL
    "Developer/Platform": [], # DJ, SDK, PLATFORM, DEV-ARCH
    "Supporting/Drafts": [] # RTC, etc.
}

for d in data:
    did = d['doc_id'].upper()
    fp = d['file_path'].upper()

    if "NORTH-STAR" in did or "FOUNDING" in did or "NORTH-STAR" in fp or "FOUNDING" in fp:
        hierarchy["Foundational"].append(d)
    elif "ZRM" in did or "ZRM" in fp:
        hierarchy["ZRM (Reality Model)"].append(d)
    elif "WS-" in did or "/RATIFIED/WS-" in fp:
        hierarchy["WS (Specifications)"].append(d)
    elif "RI-" in did or "/RATIFIED/RI-" in fp:
        hierarchy["RI (Reference Implementations)"].append(d)
    elif "RSN-" in did:
        hierarchy["RSN (Reasoning)"].append(d)
    elif "CA-" in did or "CMP-" in did or "SR-" in did or "CRL-" in did:
        hierarchy["Governance/Amendments"].append(d)
    elif "DJ-" in did or "SDK-" in did or "PLATFORM" in did or "DEV-ARCH" in did:
        hierarchy["Developer/Platform"].append(d)
    else:
        hierarchy["Supporting/Drafts"].append(d)

with open('Constitutional Reviews/Discovery/02_CONSTITUTIONAL_HIERARCHY.md', 'w') as f:
    f.write("# 02 CONSTITUTIONAL HIERARCHY\n\n")
    for layer, docs in hierarchy.items():
        f.write(f"## {layer}\n")
        for d in docs:
            f.write(f"- **{d['doc_id']}**: {d['title']} ({d['file_path']})\n")
        f.write("\n")

    f.write("## Authority Flow\n\n")
    f.write("```mermaid\ngraph TD\n")
    f.write("  NS[North Star] --> FP[Founding Principles]\n")
    f.write("  FP --> ZRM[Zyppi Reality Model]\n")
    f.write("  ZRM --> WS[Specifications]\n")
    f.write("  WS --> RI[Reference Implementations]\n")
    f.write("  RI --> SDK[SDKs]\n")
    f.write("  Governance[Governance/Amendments] -.-> ZRM\n")
    f.write("  Governance -.-> WS\n")
    f.write("```\n")
