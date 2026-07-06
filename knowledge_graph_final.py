import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

with open('Constitutional Reviews/Discovery/07_KNOWLEDGE_GRAPH.md', 'w') as f:
    f.write("# 07 KNOWLEDGE GRAPH\n\n")
    f.write("## Constitutional Knowledge Flow\n\n")
    f.write("```mermaid\ngraph LR\n")

    # Connect top concepts to defining docs
    top_concepts = ["REALITY", "INTENT", "TRUST", "ACTOR", "IDENTITY", "REFERENT", "SURFACE", "OBSERVER", "EVENT", "EVIDENCE"]
    for concept in top_concepts:
        if concept in concepts:
            cdata = concepts[concept]
            doc_id = cdata['owning_document'].split('/')[-1].replace('.md', '')
            f.write(f"  {concept}([Concept: {concept}]) --> {doc_id}[[{doc_id}]]\n")

    f.write("\n  subgraph Documents\n")
    for d in data[:10]: # Sample connections
        did = d['doc_id'].replace(' ', '_')
        if did != "Unknown":
            for ref in d['doc_refs'][:2]:
                f.write(f"    {did} --> {ref}\n")
    f.write("  end\n")
    f.write("```\n")

# Summary & Findings refinement
with open('Constitutional Reviews/Discovery/08_DISCOVERY_FINDINGS.md', 'w') as f:
    f.write("# 08 DISCOVERY FINDINGS\n\n")
    f.write("## 1. Document Families Discovered\n")
    f.write("- **ZRM (Zyppi Reality Model):** The foundational ontology and reality math.\n")
    f.write("- **WS (Workstream Specs):** 17 clusters of architectural specifications.\n")
    f.write("- **RI (Reference Implementations):** Executable truth and compiler stages.\n")
    f.write("- **RSN (Reasoning):** Decision frameworks and logic.\n")
    f.write("- **CA/A (Amendments):** Formal changes to the constitution.\n")
    f.write("- **DJ/SDK:** Developer platform and interface contracts.\n")
    f.write("- **RTC (Roundtables):** Collaborative ratification artifacts.\n")
    f.write("- **Economic:** ZEA/NEA/EAA series for economic architecture.\n\n")

    f.write("## 2. Anomalies & Observations\n")
    f.write("- **Supersession Complexity:** SR-001 (Supersession Register) is a critical artifact for resolving the 'Active Constitutional View' (ACV).\n")
    f.write("- **Version Drift:** North Star exists in v4.0 and v5.0; Founding Principles in v3, v4.2, and unversioned.\n")
    f.write("- **Naming Collisions:** Multiple files named 'ZRM-003-MASTER-BLUEPRINT.md' in different folders (e.g., constitution/ vs constitution/ratified/ZRM-003/).\n")
    f.write("- **Reserved Domains:** References to 'FED Series' and 'MARKETPLACE-SPEC-001' exist without corresponding documents.\n")
