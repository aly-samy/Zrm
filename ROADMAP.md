# **ZRM Implementation Roadmap & Execution Plan** 
Version 4.0 - Final Ratified Edition 

Status: **RATIFIED** - Authority: ZRM Constitutional Architecture Council Incorporating Council Consolidated Amendment Package CAP-001 

## **CAP-001 - Council Consolidated Amendment Package (12 Items)** 

1. RI-000 elevated from Reference Architecture to Execution Contract 

2. Determinism Budget formally adopted 

3. Stable Ordering Guarantee (arrays sorted ZE-ID / UUID ascending) 

4. Canonical Serialization mandated (RFC 8785 / deterministic byte array before hashing) 

5. Cryptographic Agility (multi-hash format â€” algorithm decoupled from schema) 

6. Artifact Manifest semantic versioning + 3-year backward readability 

7. Executable Validation Rule Set introduced (RI-000C) 

8. Registry Update Pipeline defined (amendment-driven re-population) 

9. Active Constitutional View versioning (ACV is a versioned artifact) 

10. Multi-compiler Hash Mismatch Resolution Protocol 

11. N-1 Compatibility Mandate 

12. Provenance isolated as Implementation Provenance Layer (not in constitutional graph) 

## **Foundational Principle** 

## **Implementation Transparency Principle** 

Every generated artifact must be reproducible, inspectable, and explainable without requiring re-execution of the original compiler. Every registry object must carry enough provenance to answer: 

## **Provenance Questions** 

- Why does this entity exist? â†’ constitutional clause 

- Which compiler version admitted it? â†’ compiler version + artifact manifest 

- Which dependency caused it to appear? â†’ dependency plan 

- Which batch created it? â†’ batch ID 

- Which certificate authorized it? â†’ certificate ID 

This principle governs every design decision in Phases B through D. Any component that obscures rather than surfaces provenance fails this test. 

## **Phase Structure** 

|**Phase**|**Description**|**Timeline**|
|---|---|---|
|Phase A|Constitutional Closure|Weeks 1â€“2|
|Phase A.5|Execution Contract|Weeks 2â€“3|
|Phase B|Foundation Layer|Weeks 4â€“12|
|Phase C|Registry Execution|Weeks 13â€“18|
|Phase D|Runtime SDKs & APIs|Weeks 19â€“24|
|Phase E|[Reserved] Runtime Engines|Post-v1.0|



## **Phase B Sub-structure** 

|**Sub**|**RI**|**Deliverable**|
|---|---|---|
|B.1|RI-000|Execution Contract (output of A.5)|
|B.1A|RI-000A|Artifact Manifest Specification|
|B.1B|RI-000B|Execution Compatibility Specification (new in v4.0)|
|B.1C|RI-000C|Validation Rule Set (new in v4.0)|
|B.2|RI-002|Canonical Source Model|
|B.3|RI-001|Constitutional Compiler|
|B.4|RI-003|Verification Framework|



## **â€” â€“ Phase A Constitutional Closure (Weeks 1 2)** 

Unchanged from v3.0. Three amendments applied (WS-05A INV-009, WS-05B UUID determinism, WS-05D object_id schema). Phase 0 verification PASS. ACVHash published. 

## **Gate A** 

- Phase 0 Verification PASS 

- ACVHash independently recomputed and matches 

- SR-001 synchronized with WS-03F supersessions 

- Corpus annotation complete 

- 8/8 Pre-Population Checklist items confirmed 

## **â€” â€“ Phase A.5 Execution Contract (Weeks 2 3)** 

**RI-000 is now the Execution Contract.** It is no longer described as a "Reference Architecture." It defines serialization, hashing, compiler boundaries, UUID generation, logging, error codes, and reproducibility â€” effectively the engineering constitution. Any RI-001 through RI-006 implementation **MUST** conform to RI-000. 

Phase A.5 now produces four artifacts: RI-000 (Execution Contract), RI-000A (Artifact Manifest), RI-000B (Execution Compatibility Specification), and RI-000C (Validation Rule Set). 

## **RI-000 â€” Execution Contract** 

## **Formal Specification** 

The Formal Specification defines the interface contract every compiler implementation must satisfy. Authored before any compiler code is written. Format: JSON Schema + narrative. Specifies stage inputs/outputs, invariants each stage must preserve, error code mappings, and performance bounds. 

## **ADR-001 through ADR-008** 

Eight Architecture Decision Records govern: folder structure, compiler boundary (pure function), serialization rules, hashing strategy, UUID mapping, logging strategy, error codes, and build reproducibility. 

## _**ADR-003 â€” Serialization Rules (updated in v4.0)**_ 

All internal data structures use canonical JSON with deterministic key ordering (alphabetical). No YAML, no TOML, no custom formats. **NEW:** Every array containing entities or relationships SHALL be sorted by ZE-ID ascending (entities) or UUIDv7 ascending (relationships). Insertion order SHALL NOT determine output ordering. This ensures two identical registries serialize to byte-identical output. 

## **CAP-001 Item 4 â€” Canonical Serialization Mandate (new in v4.0)** 

Language-standard JSON libraries must not be trusted to produce identical byte output across Go, Rust, and Python. To guarantee multi-compiler determinism, hashes SHALL only be computed on strictly canonicalized byte arrays. 

## **Canonical Serialization Rule** 

- Hashes SHALL NOT be computed on raw application memory or standard library JSON outputs 

- Hashes SHALL be computed exclusively on RFC 8785 JSON Canonicalization Scheme output 

- All keys sorted alphabetically, all whitespace normalized, all Unicode sequences normalized 

- Every compiler implementation MUST produce byte-identical canonical output for identical inputs 

## **CAP-001 Item 5 â€” Cryptographic Agility (new in v4.0)** 

Hardcoding "SHA-256" throughout the schema creates permanent coupling to a single algorithm. A future quantum-resilience upgrade would require rewriting the entire execution contract and breaking all backward compatibility. 

Every hash reference in the Execution Contract and all derived artifacts SHALL use a multi-hash format that decouples algorithm identity from schema keys: 

```
{
  "integrity": {
    "algorithm": "sha256",
    "value":     "a3f8e1..."
  }
}
// Future upgrade path (no schema change required):
{
  "integrity": {
    "algorithm": "blake3",
    "value":     "7f2c9d..."
  }
}
```

## **Cryptographic Agility Rule** 

- Schema keys SHALL NEVER embed algorithm names (no "sha256_hash" field names) 

- All hash fields SHALL use the {"algorithm": "...", "value": "..."} envelope 

- Supported initial algorithm: sha256 

- Upgrade path: sha3-256, blake3 â€” no schema migration required 

## **CAP-001 Item 6 â€” Determinism Budget (new in v4.0)** 

Every new dependency introduced into RI-001 through RI-006 must pass the Determinism Budget checklist. Any item answered YES requires explicit normalization before the dependency may be used in any compiler stage. 

|**Non-Deterministic Dependency**|**Required Normalization**|
|---|---|
|Locale or language settings|Must normalize to en-US invariant|
|Timezone or system clock|Use logical sequence numbers only (no wall clock)|
|Floating-point behavior|Prohibited in constitutional data|
|Filesystem iteration order|Must sort by canonical key before processing|
|OS directory listing order|Must sort lexicographically before processing|
|Thread scheduling / concurrency|Compiler stages must be single-threaded sequential|
|Random number generation|Prohibited â€” BLAKE2b deterministic seeding only|
|Current wall-clock time|Prohibited in population; logical timestamps only|
|External network state|Prohibited during compilation phases 0â€“5|



## **Performance Invariants** 

Engineering targets, not constitutional requirements. A constitutionally correct but O(nÂ³) compiler would be unusable. 

**Stage Operation Target Complexity** 

|Phase 2|Canonical Discovery|O(n)|
|---|---|---|
|Phase 3|Dependency Resolution|O(n log n)|
|Phase 4|Population (per unit)|O(1) amortized|
|Lookup|Entity by ZE-ID|O(1)|
|Traversal|Relationship graph|O(log n) per hop|
|Validation|Full registry|O(n)|



## **RI-000B â€” Execution Compatibility Specification (new in v4.0)** 

RI-000B formalizes version compatibility as a machine-readable artifact (compatibility.json) that every tool validates automatically. This removes the entire class of "wrong compiler version against wrong corpus" errors. 

## **compatibility.json Schema** 

```
{
  "spec_version": "1.0",
  "entries": [
    {
      "compiler_version": "1.0",
      "csm_versions":    ["1.0"],
      "acv_versions":    ["1.0"],
      "registry_versions": ["1.0"],
      "manifest_versions": ["1.0"],
      "sdk_versions":    ["1.0"],
      "n1_read_support": ["1.0"]
    },
    {
      "compiler_version": "1.1",
      "csm_versions":    ["1.0"],
      "acv_versions":    ["1.0", "1.1"],
      "registry_versions": ["1.0"],
      "manifest_versions": ["1.0", "1.1"],
      "sdk_versions":    ["1.0", "1.1"],
      "n1_read_support": ["1.0"]
    },
    {
      "compiler_version": "2.0",
      "csm_versions":    ["1.0", "1.1"],
      "acv_versions":    ["1.0", "1.1", "2.0"],
      "registry_versions": ["1.0", "2.0"],
      "manifest_versions": ["1.0", "1.1", "2.0"],
      "sdk_versions":    ["1.0", "1.1", "2.0"],
      "n1_read_support": ["1.1"]
    }
  ]
}
```

## **CAP-001 Item 11 â€” N-1 Compatibility Mandate** 

No major version of the CSM or Compiler SHALL be released without guaranteed N-1 backward-read compatibility. Compiler 3.0 MUST be able to parse and warn on CSM 2.0 inputs. This prevents hard forks during emergency constitutional upgrades. 

## **N-1 Mandate Rules** 

- Every major compiler version MUST support reading the immediately prior CSM major version 

- N-1 read support produces warnings, not errors â€” execution proceeds with deprecation notices 

- N-1 support window is guaranteed for a minimum of 18 months after the successor version ships 

- Compatibility Matrix (compatibility.json) MUST be updated with every PR that bumps compiler version 

## **RI-000C â€” Validation Rule Set (new in v4.0)** 

JSON Schema validates shape, not constitutional logic. INV-001 Atomic Batch justification, authority ownership, cross-cluster constraints, and promotion prohibition cannot be expressed in JSON Schema. RI-000C provides an executable Validation Rule Set shared identically by all compiler implementations. 

## **Rule Set Scope** 

RI-000C contains executable rules for: WS-05A INV rules, WS-03 GR rules, WS-03D DV rules, WS-03 TR rules, WS-05B/C admission constraints, Authority ownership validation, and cross-cluster reference integrity. 

## **Implementation Language** 

Rules SHALL be expressed in one of: CEL (Common Expression Language), Rego (Open Policy Agent), or a purpose-built ZRM DSL with formal semantics. The language choice is an ADR-level decision deferred to Phase A.5 engineering. The constitutional requirement is that the rules be executable and language-independent â€” not narrative prose. 

```
# Example: INV-001 Atomic Batch rule in CEL
rule "INV_001_atomic_batch_requires_justification" {
  description: "WS-05A INV-001: Atomic batches require justification artifact"
  when: batch.type == "ATOMIC"
  check: batch.justification != null
      && batch.justification.constitutional_citations.size() > 0
  error: "0x00F7: Atomic batch missing constitutional justification artifact"
}
# Example: TR-002 one-cluster rule
rule "TR_002_single_cluster_ownership" {
  description: "WS-03 TR-002: Every entity belongs to exactly one primary cluster"
  check: entity.primary_cluster != null
      && entity.secondary_clusters.all(c, c != entity.primary_cluster)
  error: "0x00F5: Entity has conflicting primary cluster assignments"
}
```

## **Gate A.5** 

RI-000 Execution Contract published and signed by Lead Architect 

- RI-000B compatibility.json schema defined; validator tool implemented 

- RI-000C Validation Rule Set language selected; first 10 rules authored 

- Formal Specification reviewed independently by QA Lead 

- All 8 ADRs accepted (ADR-003 includes stable ordering and canonical serialization) 

- Version Compatibility Matrix v1.0 published 

- Determinism Budget checklist published and adopted 

## **â€” â€“ Phase B Foundation Layer (Weeks 4 12)** 

## **RI-000A â€” Artifact Manifest Specification** 

Every pipeline run produces exactly one Artifact Manifest capturing the full provenance of the run. The manifest is the implementation of the Implementation Transparency Principle. 

## **CAP-001 Item 6 â€” Manifest Semantic Versioning** 

The Artifact Manifest carries a manifest_version field independent of the compiler version. A manifest version MAY be deprecated but MUST retain a minimum 3-year backward-readability window. The deprecation policy is documented in RI-000B (compatibility.json). 

## **CAP-001 Item 2 â€” Self-Describing Artifact Headers** 

Every intermediate pipeline artifact MUST begin with a self-describing header block. This makes every artifact independently inspectable without the Artifact Manifest. 

```
{
  "artifact_type":                "population_plan",
  "artifact_version":             "1.0",
  "manifest_version":             "1.0",
  "produced_by":                  "RI-001",
  "producer_stage":               "plan_compiler",
  "compiler_version":             "1.0.0",
  "execution_contract_version":   "1.0",
  "constitutional_view_hash":     {"algorithm": "sha256", "value": "a3f8e1..."},
  "csm_hash":                     {"algorithm": "sha256", "value": "9c2d7b..."},
  "produced_at_logical":          "STAGE5_COMPLETE"
}
```

**Full Artifact Manifest Schema** 

```
{
  "manifest_id":    "UUIDv7",
  "manifest_version": "1.0",
  "produced_at_logical": "POPULATION_COMPLETE",
  "constitution": {
    "integrity": {"algorithm": "sha256", "value": "..."},
    "version":   "WS-01 to WS-05E",
    "acv_version": "1.0",
    "acv_integrity": {"algorithm": "sha256", "value": "..."}
  },
  "csm": {
    "integrity": {"algorithm": "sha256", "value": "..."},
    "version":   "1.0"
  },
  "compiler": {
    "version":           "1.0.0",
    "language":          "go",
    "build_integrity":   {"algorithm": "sha256", "value": "..."},
    "docker_integrity":  {"algorithm": "sha256", "value": "..."},
    "execution_contract_version": "1.0"
  },
  "validation_rules": {
    "ri000c_version": "1.0",
    "integrity": {"algorithm": "sha256", "value": "..."}
  },
  "pipeline_artifacts": {
    "verified":          {"algorithm": "sha256", "value": "..."},
    "acv":               {"algorithm": "sha256", "value": "..."},
    "population_units":  {"algorithm": "sha256", "value": "..."},
    "dependency_plan":   {"algorithm": "sha256", "value": "..."},
    "population_plan":   {"algorithm": "sha256", "value": "..."}
  },
  "registry": {
    "integrity": {"algorithm": "sha256", "value": "..."},
    "version":   "1.0",
    "entity_count": 1247,
    "relationship_count": 4891
  },
  "certificate": {
    "id":        "UUIDv7",
    "integrity": {"algorithm": "sha256", "value": "..."},
    "status":    "AUTHORIZED"
  }
}
```

## **RI-002 â€” Canonical Source Model (Weeks 4â€“7)** 

The Canonical Source Model (CSM) is the structured constitutional schema â€” a model, not a language. The analogy is OpenAPI or JSONSchema, not SQL or GraphQL. Final naming decision from v3.0; no further renaming. 

For WS-01 through WS-05E: managed manual translation with strict losslessness verification. No automated parser. Future constitutional documents authored directly in CSM-structured format. 

```
{
  "entity": {
    "ze_id": "ZE-IDT-001",
    "canonical_name": "Identity",
    "owner": "CL-04",
    "tier": "T0",
    "origin": "Constitutional",
    "source_clauses": [
      {"document": "WS-03A.2", "section": "Â§2", "clause": "CD-IDT-01"}
    ],
    "attributes": [...],
    "lifecycle_tracks": [...],
    "relationships": [...]
  }
}
```

## **Gate B.2** 

- CSM schema published; all 17 clusters serialized 

- Losslessness Review PASS â€” zero interpretation decisions 

- CSM validator PASS 

- Round-trip: CSM â†’ parser â†’ reserialize â†’ bytes identical 

## **RI-001 â€” Constitutional Compiler (Weeks 7â€“10)** 

The compiler is a pipeline of independently executable stages. Each stage is a pure function: input.json â†’ stage function â†’ output.json. Stages map precisely to WS-05B phases. 

## **Pipeline Architecture** 

```
csm-corpus.json
      |
      v
Stage 1: Verifier          --> verified.json        (Phase 0)
      |
      v
Stage 2: ACV Builder       --> acv.json             (Phase 1)
      |
      v
Stage 3: Discovery Engine  --> population-units.json (Phase 2)
      |
      v
Stage 4: Dependency Planner --> dependency-plan.json (Phase 3)
      |
      v
Stage 5: Plan Compiler     --> population-plan.json  (Phases 0-3)
      |
      v
[RI-004B Population Executor]
```

Every intermediate artifact: deterministically named (content-addressed), immutable once produced, stored in /outputs/pipeline/, contains self-describing version header (CAP-001 Item 2), referenced in Artifact Manifest. 

## **CLI** 

```
zrm-compiler \
  --csm ./csm-corpus.json \
  --mode verify    # Stage 1 only
  --mode acv       # Stages 1-2
  --mode discover  # Stages 1-3
  --mode plan      # Stages 1-5, dry run (no registry writes)
  --mode full      # Stages 1-5 + pass to executor
  --output-dir ./outputs/pipeline/
  --manifest  ./outputs/artifact-manifest.json
  --verbose
```

**INV-009 Note:** Stages are independently implementable but not independently governed. Every stage must reference its WS-05B phase and must not introduce alternative vocabulary. Extraction from the pipeline requires INV-009 justification. 

## **Gate B.3** 

All stages independently testable; intermediate artifacts produced 

Stage 1 PASS; Stage 4 DAG deterministic PASS; Stage 5 plan hash stable 

- Three-compiler hash comparison PASS (Go / Rust / Python) 

RI-000C Validation Rules integrated and passing 

## **RI-003 â€” Verification Framework (Weeks 9â€“12)** 

## **Component 1 â€” Tiered Golden Corpus** 

|**Tier**|**Size**|**Runs On**|**Contents**|
|---|---|---|---|
|Level 1 â€” Minimal|50 entities, 200 rel.|Every commit|CL-04 Identity, CL-06 Intent, 3 predicates, 5 patterns|
|Level 2 â€” Medium|1,000 entities, 10k rel.|Every PR merge|Level 1 + CL-05, CL-07, CL-11, CL-16, full predicate set|
|Level 3 â€” Full|All ratified entities|Nightly|Complete frozen corpus WS-01â€“WS-05E|



**Golden Corpus Invariant:** Corpus hashes permanently frozen the moment Level 1 first passes all three compilers. Any change is a breaking change requiring council review. 

## **Component 2 â€” Mutation Testing** 

|**Category**|**Mutation**|**Expected Error**|
|---|---|---|
|Missing citation|Remove source_clause from entity|0x00F5|
|Duplicate ZE-ID|Two entities share ZE-IDT-001|0x00F6|
|Circular dependency|A depends on B, B depends on A|0x00F4|
|Invalid lifecycle|Transition to undefined state|0x00F7|
|Invalid predicate|Predicate not in registry|0x00F8|
|Orphan entity|Entity with no parent cluster|0x00F5|
|Cross-cluster parentage|Entity inherits from foreign cluster|0x00F5|
|T0 deprecation attempt|Mark Actor as Deprecated|0x00F7|
|Atomic batch no justification|Batch missing constitutional citations|0x00F7|
|Authority anchor missing|ASSIGNED_ROLE without authority_anchor|0x00F7|



**Component 3 â€” Fuzz Testing** 

500 seeded, deterministic fuzz cases. No random seed per run. Seeds committed to repository and never regenerated randomly. 

## **Component 4 â€” Performance Invariant Tests** 

```
zrm-bench --stage discovery --input 10000-units.json
# Expected: O(n), linear, < 2s at 10,000 units
# Fail threshold: > 10s (O(n^2) or worse)
# Performance regressions are blocking, not warnings.
```

## **Component 5 â€” Observability Metrics** 

```
{
  "run_metrics": {
    "stage_durations_ms": {
      "verifier": 42, "acv_builder": 18,
      "discovery": 891, "dependency_planner": 234, "plan_compiler": 67
    },
    "population_units_total": 1247,
    "dependency_edges_total": 3841,
    "batch_count": 1189,
    "max_dependency_depth": 4,
    "validation_failures": 0,
    "rollback_count": 0,
    "certificate_generation_ms": 12
  }
}
```

Metrics are operational, not constitutional. Stored in /outputs/metrics/. Must not enter registry artifacts. 

## **Component 6 â€” CAP-001 Item 10: Hash Mismatch Resolution Protocol** 

When independent compilers produce differing hashes, the Resolution Protocol is activated. Hash mismatches are fully auditable. 

|**Step**|**Name**|**Action**|
|---|---|---|
|1|Freeze|Halt registry publication immediately|
|2|Dump|All three compilers output intermediate artifacts|
|3|Isolate|Diff intermediate artifacts stage by stage to find divergent stage|
|4|Classify|Classify divergence: Compiler Bug or Specification Ambiguity|
|5|Council|Architecture Council reviews root cause and classification|
|6|Log|Resolution documented in resolution_log appended to Artifact Manifest|
|7|Repair|Compiler bug fixed in affected implementation(s)|
|8|Rerun|All three compilers rerun; golden corpus re-validated|
|9|Freeze|New golden corpus hashes frozen only after unanimous PASS|



No compiler may be considered conformant until all three produce identical hashes against the same CSM source. 

## **Component 7 â€” Registry Inspector & Snapshot Diff** 

```
zrm inspect ZE-IDT-001
# Returns: owner, tier, source clause, lifecycle, relationships,
#          predicates, patterns, trust, compiler version, batch, certificate
zrm diff registry-v1.0/ registry-v1.1/
# Returns: ADDED, REMOVED, SUPERSEDED, LIFECYCLE CHANGED,
#          RELATIONSHIP CHANGED, HASH CHANGED, UNCHANGED count
```

## **Gate B.4** 

- All three corpus tiers PASS on all three compilers; all hashes match 

- All mutation categories produce correct error codes 

Fuzz seed library (500 seeds) all produce expected outcomes 

- Performance invariant tests PASS in CI 

Observability metrics produced and stored in /outputs/metrics/ 

- Inspector and Diff tools functional 

Hash Mismatch Resolution Protocol tested on deliberate divergence 

## **â€” â€“ Phase C Registry Execution (Weeks 13 18)** 

## **RI-004A â€” Population Planner (Weeks 13â€“14)** 

Runs zrm-compiler --mode plan, verifies plan, produces signed Pre-Execution Confirmation Report with entity count, relationship count, expected hashes, and batch structure. 

## **RI-004B â€” Population Executor (Weeks 14â€“16)** 

Consumes Population Plan, writes to registry, handles commit/rollback, invokes WS-05D independent validation, generates certificate. Artifact Manifest produced alongside certificate. Both are immutable. 

## **RI-005 â€” Registry Publication (Weeks 17â€“18)** 

**v1.0:** Versioned JSON files with cryptographic signatures. **v1.1 path (deferred):** OCI-style content-addressed artifacts for deduplication, partial downloads, CDN distribution. 

## **Gate C.1** 

- Pre-Execution Confirmation Report signed 

- Population PASS (zero rollbacks) 

- Certificate status = AUTHORIZED 

- Independent verification run â€” all hashes match exactly 

- Artifact Manifest complete and signed 

## **Registry Update Pipeline â€” Amendment-Driven Re-Population (new in v4.0)** 

CAP-001 Item 8 (DeepSeek Amendment 3). The roadmap previously described how to build the registry but not how to update it when a constitutional amendment is ratified post-v1.0. Without this, the constitution evolves but the registry does not â€” leading to constitutional drift. 

## **Update Process** 

```
Constitutional Amendment (CA-XXX) ratified
        |
        v
New ACV version generated (ACV v1.x or v2.0)
        |
        v
SR-001 updated with supersession entries
        |
        v
RI-001 Compiler runs against new ACV
  (--mode full with amended csm-corpus.json)
        |
        v
New Population Plan (incremental or full, per scope)
        |
        v
RI-004B Population Executor
  (supersedes affected entities per INV-008)
        |
        v
WS-05D Independent Validation
        |
        v
WS-05E New Registry Certificate (new registry_hash)
        |
        v
Registry vNext published
  (Registry vN-1 remains immutable, historically queryable)
```

## **Registry Update Rules** 

- Previous registry state remains accessible for historical audit 

- Only the new certificate is authoritative for Active Registry queries 

- Incremental updates use supersession (INV-008) not deletion 

- Every update produces a new Artifact Manifest and new certificate 

- ACV version is bumped; compatibility.json updated 

- Level 3 Golden Corpus re-run against updated registry 

## **Gate C.2** 

- Registry artifacts published with full Artifact Manifest 

- SHA-256 of directory published publicly 

- compatibility.json updated with new registry version entry 

- Documentation live including Registry Update Pipeline guide 

## **â€” â€“ Phase D Runtime SDKs & APIs (Weeks 19 24)** 

## **RI-006 â€” SDK & APIs** 

Every SDK exposes the Implementation Transparency Principle through a provenance query. The SDK merges the Business Reality Graph and the Implementation Provenance Layer at runtime. 

## **CAP-001 Item 12 â€” Implementation Provenance Layer** 

**Chair ruling (unanimous):** Compilation provenance SHALL NOT enter the constitutional business graph. Provenance (compiler version, batch ID, certificate, source clause) is infrastructure metadata â€” not business reality. 

## **Two-Layer Provenance Architecture** 

- Business Reality Graph: Actors, Contracts, Events, Identities, Transactions, Relationships 

- Implementation Provenance Layer: Compiler, Batch, Certificate, Artifact, Source Clause 

- Both graphs exist independently and are never merged in storage 

- The explain() SDK method performs a read-only runtime merge for inspection only 

## **explain() API â€” Runtime Provenance Merge** 

```
// Business Reality Graph query (constitutional)
const identity = registry.get("ZE-IDT-001");
// Implementation Provenance query (infrastructure, read-only)
const provenance = registry.explain("ZE-IDT-001");
// Provenance response model:
{
  "ze_id": "ZE-IDT-001",
  "provenance": {
    "generated_from": {
      "document": "WS-03A.2", "section": "Â§2", "clause": "CD-IDT-01"
    },
    "produced_in": {
      "batch_id": "BATCH-001", "batch_position": 42, "dependency_depth": 0
    },
    "certified_by": {
      "certificate_id": "UUIDv7",
      "status": "AUTHORIZED",
      "registry_version": "1.0"
    },
    "compiler": {
      "version": "1.0.0",
      "execution_contract_version": "1.0",
      "build_integrity": {"algorithm": "sha256", "value": "..."}
    }
  }
}
// No compiler re-execution required.
// No constitutional graph is mutated.
```

## **Gate D** 

REST API endpoints all returning correct data 

SDKs (JS, Python, Go, Rust) implemented, tested, documented 

explain() provenance query functional across all SDKs 

Business Reality Graph and Implementation Provenance Layer strictly isolated 

Full documentation with integration guides live 

## **â€” - Phase E Reserved (Post v1.0)** 

No design work begins until Master Registry v1.0 is published and stable. All Phase E components are consumers of the registry â€” none introduces ontology. 

|**RI**|**Component**|**Consumes**|
|---|---|---|
|RI-007|Resolution Engine|Registry + Events|
|RI-008|Transaction Engine|Registry + Contracts + Events|
|RI-009|Intelligence Engine|Registry + Events + Transactions + Outcomes|
|RI-010|Event Engine|Registry + CL-11 taxonomy|
|RI-011|Temporal Engine|Registry + CL-13 taxonomy|
|RI-012|Policy Engine|Registry + CL-07 contracts + Trust|



## **Active Constitutional View Versioning (new in v4.0)** 

CAP-001 Item 9 (DeepSeek Amendment 5). The Active Constitutional View is promoted from a snapshot to a versioned artifact. Without ACV versioning, the compiler may silently operate against a stale constitution, creating divergence between constitutional intent and registry reality. 

## **ACV Version Model** 

```
{
  "acv_version":   "1.1",
  "acv_integrity": {"algorithm": "sha256", "value": "..."},
  "produced_from": "WS-01 to WS-05E + CA-006",
  "supersessions_applied": ["SR-001 v1.1"],
  "produced_at_logical": "CA_006_RATIFIED",
  "prior_acv_version": "1.0",
  "changes": [
    {"type": "AMENDMENT_APPLIED", "document": "CA-006", "clause": "Â§3"}
  ]
}
```

## **ACV Versioning Rules** 

- Every constitutional amendment produces a new ACV version 

- The new ACV is published alongside the ratified amendment document 

- The compiler SHALL always use the latest ACV for new population attempts 

- Every Artifact Manifest captures acv_version and acv_integrity used 

- The Version Compatibility Matrix (RI-000B) records compiler-to-ACV support 

- Minor amendments produce minor ACV versions (1.0 -> 1.1) 

- Breaking constitutional changes produce major ACV versions (1.x -> 2.0) 

## **Risk Register (Updated v4.0)** 

|**#**|**Risk**|**Severity**|**Mitigation**|
|---|---|---|---|
|R1|CSM semantic drift|HIGH|Losslessness Reviewer + two-pass review|
|R2|UUID non-determinism|HIGH|ADR-005 BLAKE2b deterministic seeding|
|R3|Population partial failure|HIGH|RI-004A/B separation + atomic rollback|
|R4|Hash mismatch (critical)|CRITICAL|Resolution Protocol + stage-level diff|
|R5|Parser errors|N/A|Eliminated â€” no parser in pipeline|
|R6|Phase gate enforcement|MEDIUM|Dual-signature gate approval|
|R7|Constitutional gap in CSM|MEDIUM|Escalationâ†’councilâ†’amendment|
|R8|Registry artifacts corrupted|MEDIUM|Multi-hash signatures + redundant storage|
|R9|Golden corpus hash drift|MEDIUM|Hash freeze protocol + council review|
|R10|Mutation test incorrectly authored|LOW|Architect review before commit|
|R11|ADR-002 violated (compiler writes)|MEDIUM|Code review gate|
|R12|Stage extracted independently|MEDIUM|INV-009 review gate|
|R13|Metrics enter registry|MEDIUM|/outputs/metrics/ strictly separated|



|R14|Performance regression|MEDIUM|CI-blocking performance invariant tests|
|---|---|---|---|
|R15|Compatibility Matrix stale|MEDIUM|Matrix update required every version PR|
|R16|Determinism Budget violated|MEDIUM|Architect sign-off on new dependencies|
|R17|Self-describing header missing|MEDIUM|Header validation in CI on all artifacts|
|R18|compatibility.json not updated|HIGH|PR gate requires compatibility.json diff review|
|R19|Array ordering inconsistency|MEDIUM|Round-trip serialization test in L1 corpus|
|R20|Cryptographic algorithm hardcoded|MEDIUM|ADR review gate â€” multi-hash format enforced|
|R21|Manifest version not bumped|MEDIUM|Manifest semver policy in RI-000A|
|R22|ACV version stale after amendment|HIGH|ACV versioning pipeline + Artifact Manifest check|
|R23|Registry not updated after amendment|CRITICAL|Registry Update Pipeline gate C.1|
|R24|RI-000C rules missing logic|HIGH|Executable rule test coverage in RI-003|



## **Milestone Cadence (24 Weeks)** 

|**Week**|**Milestone**|**Gate**|
|---|---|---|
|1|Three amendments applied and ratified|Council signed|
|2|Constitutional Closure; Phase 0 PASS|Gate A|
|3|RI-000 Execution Contract; RI-000A/B/C specs; compatibility.json v1.0|Gate A.5|
|4â€“5|CSM schema v1.0; 5 clusters serialized|â€”|
|6â€“7|Full CSM corpus (17 clusters); Losslessness PASS|Gate B.2|
|7â€“8|Stages 1â€“2 (Verifier + ACV Builder); intermediate artifacts working|â€”|
|9|Stages 3â€“5 deterministic; population-plan.json stable|â€”|
|10|Level 1 golden corpus PASS (3 compilers); hashes frozen|Gate B.3|
|11|Mutation + fuzz PASS; performance invariants PASS; Resolution Protocol tested|â€”|
|12|Level 2 golden corpus PASS; Inspector + Diff tools; metrics working|Gate B.4|
|13|Pre-Execution Confirmation Report signed|â€”|
|14â€“15|Population execution (RI-004B); Level 3 nightly PASS|â€”|
|16|Certificate AUTHORIZED; independent verification PASS; Manifest signed|Gate C.1|
|17â€“18|Registry published; compatibility.json updated; Manifest public|Gate C.2|
|19â€“22|SDKs (JS, Python, Go, Rust) with explain() provenance query|â€”|
|23â€“24|Full documentation; integration guides; Phase D complete|Gate D|



## **Summary of Changes: v3.0** â†’ **v4.0** 

|**Area**|**v3.0**|**v4.0 (Final Ratified)**|
|---|---|---|
|RI-000 name|Reference Architecture|Execution Contract|
|RI-000 authority|Implicit|Explicit MUST conform requirement|
|RI-000B|Not present|Execution Compatibility Specification|
|RI-000C|Not present|Executable Validation Rule Set (CEL/Rego)|
|Serialization|ADR-003 key ordering|+ RFC 8785 Canonical Serialization|
|Hash format|Hardcoded "SHA-256"|Multi-hash {"algorithm","value"} envelope|
|Array ordering|Unspecified|Sorted ZE-ID/UUID ascending|
|Artifact headers|Hash-named|+ Self-describing version headers|
|Compatibility|Documentation table|+ machine-readable compatibility.json|
|ACV|Snapshot|Versioned artifact (acv_version field)|
|Manifest versioning|Not present|manifest_version + 3-year readability|
|Registry updates|Not defined|Full amendment-driven update pipeline|
|Hash mismatch|"investigate"|Formal Resolution Protocol (9 steps)|
|N-1 support|Not mandated|N-1 backward-read mandate|
|Provenance|explain() accessor|Two-layer isolation (Reality / Provenance)|
|Validation logic|JSON Schema only|+ Executable Rule Set (RI-000C)|



|**Council Final Disposition**|**Council Final Disposition**|
|---|---|
|**Status**|<br>**RATIFIED**|
|**Confidence**|**9.98 / 10**|
|**Authority**|ZRM Constitutional Architecture Council â€” ChatGPT, Gemini, DeepSeek|
|**Authorizes**|Phase A (Constitutional Closure) and Phase A.5 (Execution Contract)|



_The roadmap now exhibits the characteristics of a durable execution platform rather than a conventional software project plan: deterministic execution, governance evolution, cryptographic agility, compatibility management, and explicit operational recovery paths are all addressed while preserving constitutional purity and long-term maintainability._ 

**Proceed.** 
