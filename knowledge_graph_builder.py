import json

with open('raw_metadata.json', 'r') as f:
    metadata = json.load(f)
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

with open('Constitutional Reviews/Discovery/07_KNOWLEDGE_GRAPH.md', 'w') as f:
    f.write("# 07 KNOWLEDGE GRAPH\n\n")
    f.write("This graph represents the flow of constitutional knowledge from core concepts to the documents that define and use them.\n\n")
    f.write("```mermaid\ngraph LR\n")

    # Map first 20 concepts to their defining docs
    count = 0
    for concept, data in concepts.items():
        if count > 30: break
        doc_name = data['owning_document'].split('/')[-1].replace('.md', '')
        f.write(f"  {concept}([Concept: {concept}]) --> {doc_name}\n")
        count += 1

    f.write("```\n")

# Report 08: DISCOVERY_FINDINGS.md
with open('Constitutional Reviews/Discovery/08_DISCOVERY_FINDINGS.md', 'w') as f:
    f.write("# 08 DISCOVERY FINDINGS\n\n")
    f.write("## Observations\n\n")

    unknown_ids = [m["file_path"] for m in metadata if m["doc_id"] == "Unknown"]
    f.write(f"### Documents with Missing ID ({len(unknown_ids)})\n")
    for path in unknown_ids:
        f.write(f"- {path}\n")

    f.write("\n### Document Families Discovered\n")
    f.write("- ZRM (Zyppi Reality Model)\n- WS (Workstream Specifications)\n- RI (Reference Implementations)\n- RSN (Reasoning)\n- DJ (Developer Journeys)\n- SDK (Software Development Kit)\n- CA/A (Amendments)\n- RTC (Roundtable Conversations)\n")

    f.write("\n### Anomalies\n")
    f.write("- Multiple versions of North Star and Founding Principles found in different directories.\n")
    f.write("- Significant number of 'RTC' (Roundtable) documents in the ratified folder, suggesting a collaborative ratification history.\n")
    f.write("- Large volume of ZRM-003 sub-documents (Stages 1-5).\n")

# Report 09: DISCOVERY_EXECUTIVE_SUMMARY.md
with open('Constitutional Reviews/Discovery/09_DISCOVERY_EXECUTIVE_SUMMARY.md', 'w') as f:
    f.write("# 09 DISCOVERY EXECUTIVE SUMMARY\n\n")
    f.write("## 1. Overview\n")
    f.write(f"The Zyppi constitutional corpus consists of approximately {len(metadata)} documents spanning Philosophy, Reality, Structure, Governance, Execution, Publication, and Runtime layers.\n\n")

    f.write("## 2. Key Metrics\n")
    f.write(f"- **Total Documents:** {len(metadata)}\n")
    f.write("- **Primary Document Families:** ZRM, WS, RI, RSN, SDK, DJ, CA, RTC\n")
    f.write("- **Mapping Confidence:** High (based on automated extraction and structural analysis)\n\n")

    f.write("## 3. Maturity Assessment\n")
    f.write("The corpus exhibits a high degree of maturity in Reality Modeling (ZRM) and structural specifications (WS). Runtime and Publication layers appear to be in active development or earlier stages.\n\n")

    f.write("## 4. Strengths\n")
    f.write("- Extremely granular decomposition of 'Reality' into math, ontology, and primitives.\n")
    f.write("- Clear naming conventions for major document series.\n")
    f.write("- Extensive cross-referencing between specifications.\n\n")

    f.write("## 5. Weaknesses (Descriptive)\n")
    f.write("- Version drift across top-level and subdirectory documents.\n")
    f.write("- Discovery of 'orphaned' or missing references (e.g., FED series mentioned in DJ-008 but not found).\n")
    f.write("- High complexity in the ZRM-003 branch may require better navigation aids.\n")
