# Council Structure

## Constitutional Architecture Council

Chair
├── ChatGPT
│    Strategic architecture
│    Cross-document synthesis
│
├── Claude
│    Governance
│    Semantic architecture
│    Constitutional consistency
│
├── Gemini
│    Determinism
│    Serialization
│    Survivability
│
├── DeepSeek
│    Operational execution
│    Validation
│    Delivery
│
└── Jules
     Implementation auditor
     Prototype builder
     Simulation engine
     CI verifier


---

## Jules Mission

Instead of asking

> "What do you think?"



ask

> "Implement this specification exactly as written and report every ambiguity, contradiction, missing definition, hidden assumption, and implementation risk."




---

## Repository Organization

I would organize the repository as a constitutional project rather than a software project.

zrm/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
│
├── constitution/
│   │
│   ├── ratified/
│   │    ├── RI-000.md
│   │    ├── RI-001.md
│   │    ├── RI-002.md
│   │    ├── CR-001.md
│   │    ├── WS-00A.md
│   │    ├── ...
│   │
│   ├── amendments/
│   │
│   └── archives/
│
├── csm/
│   │
│   ├── schemas/
│   ├── corpus/
│   ├── examples/
│   └── validation/
│
├── compiler/
│   │
│   ├── specification/
│   ├── reference-tests/
│   └── fixtures/
│
├── council/
│   │
│   ├── roundtables/
│   │
│   │     RT-001/
│   │     RT-002/
│   │     RT-003/
│   │     RT-004/
│   │     RT-005/
│   │     RT-006/
│   │
│   ├── decisions/
│   └── reports/
│
├── implementation/
│   │
│   ├── go/
│   ├── rust/
│   ├── python/
│   └── reference/
│
├── simulations/
│   │
│   ├── stage1/
│   ├── stage2/
│   ├── stage3/
│   ├── stage4/
│   └── stage5/
│
├── tests/
│   │
│   ├── golden/
│   ├── integration/
│   ├── regression/
│   └── determinism/
│
└── reports/
    │
    ├── jules/
    ├── council/
    └── certification/


---

## Jules Workflow

Every Roundtable should generate a Jules mandate.

Council ratifies proposal

↓

Jules receives implementation mandate

↓

Jules creates prototype

↓

Jules executes simulation

↓

Jules executes edge cases

↓

**Jules identifies:**

- contradictions
- missing definitions
- ambiguous wording
- impossible requirements
- hidden dependencies
- determinism risks

↓

Jules publishes Implementation Report

↓

Council reviews report

↓

Architecture updated if necessary


---

## Branch Strategy

main
│
├── constitution/*
│
├── csm/*
│
├── ri001/*
│
├── ri002/*
│
└── experiments/*

Never develop directly on main.

Every roundtable gets its own branch.

rt006-csm

rt007-ri003

rt008-runtime


---

## Labels

Use GitHub Issues with standardized labels.

constitutional

governance

serialization

determinism

implementation

ambiguity

risk

breaking-change

needs-council

needs-jules

simulation

validated

ratified


---

## Jules Deliverables

Every implementation review should produce the same structure.

### Jules Report

1.
Implementation Summary

2.
Specification Coverage

3.
Missing Definitions

4.
Hidden Assumptions

5.
Contradictions

6.
Edge Cases

7.
Determinism Audit

8.
Simulation Results

9.
CI Results

10.
Recommendations

11.
Risk Matrix

12.
Council Questions


---

## Simulation Matrix

Have Jules simulate every RI-001 stage independently.

### Stage 1
Verifier

✓ valid manifest

✓ corrupted manifest

✓ missing document

✓ broken SR-001

✓ annotation failure

----------------------

### Stage 2
ACV Builder

✓ supersession chain

✓ ontology cycles

✓ orphan nodes

✓ invariant violations

----------------------

### Stage 3

✓ discovery completeness

✓ duplicate discovery

✓ ordering stability

----------------------

### Stage 4

✓ dependency graph

✓ atomic batch

✓ topological ordering

----------------------

### Stage 5

✓ UUID generation

✓ ZE-ID allocation

✓ provenance

✓ manifest generation

✓ reproducibility


---

## Golden Rule

I would also add one permanent instruction for Jules:

> Never attempt to "fix" architectural ambiguity. Implement exactly what is specified. Whenever multiple valid implementations exist, stop and generate an Implementation Ambiguity Report instead of making assumptions. Every assumption is a constitutional defect that must be resolved by the Council.

---

This turns Jules into an objective implementation auditor rather than another design participant, giving the Council continuous feedback on whether its specifications are truly executable.