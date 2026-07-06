import json

with open('deep_analysis.json', 'r') as f:
    data = json.load(f)
with open('raw_concepts.json', 'r') as f:
    concepts = json.load(f)

with open('Constitutional Reviews/Discovery/07_KNOWLEDGE_GRAPH.md', 'w') as f:
    f.write("# 07 KNOWLEDGE GRAPH\n\n")
    f.write("## Constitutional Knowledge Flow\n\n")
    f.write("```mermaid\ngraph LR\n")

    # Map key concepts to documents
    for concept in ["REALITY", "INTENT", "TRUST", "ACTOR", "IDENTITY", "REFERENT", "SURFACE", "OBSERVER", "EVENT", "EVIDENCE"]:
        if concept in concepts:
            doc_id = concepts[concept]['owning_document'].split('/')[-1].replace('.md', '').replace(' ', '_').replace('-', '_')
            f.write(f"  {concept}([Concept: {concept}]) --> {doc_id}\n")

    f.write("\n  subgraph Documents\n")
    # Link some key documents
    f.write("    NORTH_STAR --> FOUNDING_PRINCIPLES\n")
    f.write("    FOUNDING_PRINCIPLES --> ZRM_V1_1\n")
    f.write("    ZRM_V1_1 --> WS_03A_0\n")
    f.write("    WS_03A_0 --> RI_001\n")
    f.write("  end\n")
    f.write("```\n")
