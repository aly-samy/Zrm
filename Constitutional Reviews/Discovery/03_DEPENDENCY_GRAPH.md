# 03 DEPENDENCY GRAPH


```mermaid
graph TD
  PRD --> **
  PRD --> /NORTH_STAR.md
  TECH-ARCH --> -
  TECH-ARCH --> /NORTH_STAR.md
  RI-001 --> RI-000
  RI-001 --> Execution
  RI-001 --> Contract
  RI-001 --> v1.0
  RI-002 --> RI-000
  RI-002 --> Execution
  RI-002 --> Contract
  RI-002 --> v1.0
  RI-003 --> RI-000
  RI-003 --> Execution
  RI-003 --> Contract
  RI-003 --> v1.0
  RI-004 --> RI-000
  RI-004 --> Execution
  RI-004 --> Contract
  RI-004 --> v1.0
  -_Actor_parent_of_Referent --> |
  -_Actor_parent_of_Referent --> WS-03A.0
  -_Actor_parent_of_Referent --> Cluster
  -_Actor_parent_of_Referent --> Architecture
  -_Actor_parent_of_Referent --> WS-03A.2
  -_Actor_parent_of_Referent --> Hierarchy
  -_Actor_parent_of_Referent --> Classification
  -_Actor_parent_of_Referent --> Framework
  -_Actor_parent_of_Referent --> WS-03B
  -_Actor_parent_of_Referent --> Parent
  -_Actor_parent_of_Referent --> Assignment
  -_Actor_parent_of_Referent --> Matrix
  -_Actor_parent_of_Referent --> WS-04A
  -_Actor_parent_of_Referent --> Relationship
  -_Actor_parent_of_Referent --> Governance
  -_Actor_parent_of_Referent --> Foundation
```

## Related Reports

- [00 MISSION EXECUTIVE SUMMARY](00_MISSION_EXECUTIVE_SUMMARY.md)
- [01 DOCUMENT REGISTRY](01_DOCUMENT_REGISTRY.md)
- [02 CONSTITUTIONAL HIERARCHY](02_CONSTITUTIONAL_HIERARCHY.md)
- [04 CITATION INDEX](04_CITATION_INDEX.md)
- [05 CONCEPT INDEX](05_CONCEPT_INDEX.md)
- [06 DOCUMENT SUMMARIES](06_DOCUMENT_SUMMARIES.md)
- [07 KNOWLEDGE GRAPH](07_KNOWLEDGE_GRAPH.md)
- [08 DISCOVERY FINDINGS](08_DISCOVERY_FINDINGS.md)
- [09 DIRECTORY RESTRUCTURE PROPOSAL](09_DIRECTORY_RESTRUCTURE_PROPOSAL.md)
- [10 MIGRATION PLAN](10_MIGRATION_PLAN.md)
- [11 DUPLICATE AND SUPERSESSION ANALYSIS](11_DUPLICATE_AND_SUPERSESSION_ANALYSIS.md)
- [12 CANONICAL NAMING STANDARD](12_CANONICAL_NAMING_STANDARD.md)
- [13 ORPHAN ANALYSIS](13_ORPHAN_ANALYSIS.md)
- [14 CONFLICT ANALYSIS](14_CONFLICT_ANALYSIS.md)
- [15 GAP ANALYSIS](15_GAP_ANALYSIS.md)
- [16 AI NAVIGATION INDEX](16_AI_NAVIGATION_INDEX.md)
- [17 REPOSITORY HEALTH SCORE](17_REPOSITORY_HEALTH_SCORE.md)
