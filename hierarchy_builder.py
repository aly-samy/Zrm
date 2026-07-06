import json

with open('raw_metadata.json', 'r') as f:
    metadata = json.load(f)

# Heuristic for hierarchy: RI/WS/RSN prefixes and specific files
layers = {
    "Philosophy": [],
    "Reality": [],
    "Structure": [],
    "Governance": [],
    "Execution": [],
    "Publication": [],
    "Runtime": [],
    "Unknown": []
}

for m in metadata:
    fp = m["file_path"].lower()
    if "north-star" in fp or "founding-principle" in fp:
        layers["Philosophy"].append(m["doc_id"])
    elif "zrm" in fp or "arm" in fp:
        layers["Reality"].append(m["doc_id"])
    elif "ws-03" in fp:
        layers["Structure"].append(m["doc_id"])
    elif "ca-" in fp or "cmp" in fp or "auth" in fp:
        layers["Governance"].append(m["doc_id"])
    elif "ri-001" in fp or "ri-000" in fp or "ri-004" in fp:
        layers["Execution"].append(m["doc_id"])
    elif "ri-005" in fp or "pub" in fp:
        layers["Publication"].append(m["doc_id"])
    elif "sdk" in fp or "api" in fp:
        layers["Runtime"].append(m["doc_id"])
    else:
        layers["Unknown"].append(m["doc_id"])

with open('Constitutional Reviews/Discovery/02_CONSTITUTIONAL_HIERARCHY.md', 'w') as f:
    f.write("# 02 CONSTITUTIONAL HIERARCHY\n\n")
    f.write("## Constitutional Layers\n\n")
    for layer, docs in layers.items():
        f.write(f"### {layer}\n")
        for doc in docs:
            f.write(f"- {doc}\n")
        f.write("\n")

    f.write("## Authority Chain (Mermaid)\n\n")
    f.write("```mermaid\ngraph TD\n")
    f.write("  NS[North Star] --> FP[Founding Principles]\n")
    f.write("  FP --> ZRM[Zyppi Reality Model]\n")
    f.write("  ZRM --> WS[Workstream Specifications]\n")
    f.write("  WS --> RI[Reference Implementations]\n")
    f.write("  RI --> SDK[Runtime SDKs]\n")
    f.write("```\n")

# Report 03: DEPENDENCY_GRAPH.md
with open('Constitutional Reviews/Discovery/03_DEPENDENCY_GRAPH.md', 'w') as f:
    f.write("# 03 DEPENDENCY GRAPH\n\n")
    f.write("```mermaid\ngraph TD\n")
    for m in metadata:
        if m["doc_id"] != "Unknown":
            for dep in m["depends_on"]:
                if dep != "Unknown" and dep.strip():
                    f.write(f"  {m['doc_id']} --> {dep}\n")
    f.write("```\n")

# Report 04: CITATION_INDEX.md
with open('Constitutional Reviews/Discovery/04_CITATION_INDEX.md', 'w') as f:
    f.write("# 04 CITATION INDEX\n\n")
    f.write("| Source Document | Referenced Document | Reference Type |\n")
    f.write("| --- | --- | --- |\n")
    for m in metadata:
        for ref in m["references"]:
            f.write(f"| {m['doc_id']} | {ref} | Explicit |\n")
