I recommend treating this as a **Council artifact**, not a design document.
 
Its purpose is to prevent ontology drift before anyone writes a single sentence of ZRM-002.
  
# ZRM-002-ONTOLOGY-MATRIX.md
 
**Status:** Draft v1.0
 
**Purpose:** Constitutional Design Matrix
 
**Authority:** AI Council Working Document
 
**Supports:** ZRM-002 Core Ontology
  
# 1. Purpose
 
The Ontology Matrix serves as the constitutional design map for ZRM-002.
 
It identifies every ontological concept that may appear within the Core Ontology and defines:
 
 
- whether the concept already exists,
 
- where its authority originates,
 
- whether it is permitted,
 
- what constitutional role it serves,
 
- where it may be expanded,
 
- and which downstream constitution owns future refinements.
 

 
It is **not** itself constitutional.
 
It exists solely to guarantee that ZRM-002 remains complete, minimal, and free from scope creep.
  
# 2. Constitutional Categories
 
Every ontological concept SHALL belong to exactly one category.
 
  
 
Category | Meaning
 ---|---  
Primitive | Constitutional building block defined by ZRM-001
Structural Construct | Required to describe primitives
Structural Relationship | Connects constitutional constructs
Structural Property | Immutable descriptive property
Ontological Constraint | Constitutional rule governing ontology
Deferred Concept | Belongs to downstream constitutions
Forbidden Concept | Never allowed in ZRM-002
  
# 3. Ontology Matrix
 
  
 
Concept | Category | Source | Status | Notes | Downstream Owner
---|---|---|---|---|---
Subject | Primitive | ZRM-001 | Frozen | SHALL NOT redefine | —
Object | Primitive | ZRM-001 | Frozen | SHALL NOT redefine | —
Place | Primitive | ZRM-001 | Frozen | SHALL NOT redefine | —
Event | Primitive | ZRM-001 | Frozen | SHALL NOT redefine | —
Evidence | Primitive | ZRM-001 | Frozen | SHALL NOT redefine | —
Primitive | Structural Construct | ZRM-002 | New | Common constitutional abstraction for Subject, Object, Place, Event, and Evidence. | —
Identity | Structural Relationship | ZRM-002 | New | Never a primitive | ZRM-004
Representation | Structural Construct | ZRM-002 | New | Referenced by Identity | ZRM-005
Attribute | Structural Property | ZRM-002 | New | Descriptive only | —
Relationship | Structural Relationship | ZRM-002 | New | Structural only | —
Structural Classification | Structural Property | ZRM-002 | New | Ontological only | ZRM-005
Subject Role Mapping | Structural Relationship | ZRM-002 | New | Resolves ZRM-001 Role | ZRM-005
Ontological Invariant | Ontological Constraint | ZRM-002 | New | Governs ontology | ZRM-003
Role | Structural Construct | _ | New | Temporary participation of a Subject or Object within an Event. Not a primitive.
 
# 4. Deferred Concepts
 
The following concepts SHALL NOT be defined inside ZRM-002.
 
  
 
Concept | Deferred To
---|---
Capability | ZRM-006
Permission | Execution Constitution
Role | Execution Constitution
Workflow | Execution Constitution
Trust | ZRM-004
Confidence | ZRM-004
Verification | ZRM-004
Semantic Meaning | ZRM-005
Projection | ZRM-005
Knowledge | ZRM-005
Reasoning | Reasoning Constitution
Mathematics | ZRM-003
Query | SDK
Storage | SDK
API | SDK
Database | SDK
  
# 5. Forbidden Concepts
 
The following SHALL NEVER appear in ZRM-002.
 
 
- Business Rules
 
- Pricing
 
- Inventory
 
- Permissions
 
- Authentication
 
- Authorization
 
- UI
 
- UX
 
- API Design
 
- Database Design
 
- Serialization
 
- Programming Languages
 
- Cloud Architecture
 
- Graph Engine
 
- AI Algorithms
 
- Optimization
 
- Networking
 
- Storage Technology
 

  
# 6. Identity Rule
 
Identity SHALL NOT be modeled as a Primitive.
 
Identity SHALL exist only as a constitutional relationship between:
 
 
Primitive ↔ Representation
 
 
No exception.
  
# 7. Attribute Rule
 
Attributes SHALL describe only immutable structural characteristics.
 
Attributes SHALL NOT express:
 
 
- behavior
 
- authority
 
- execution
 
- business semantics
 
- derived meaning
 

 
Examples of valid attributes:
 
 
- Name
 
- Description
 
- Valid From
 
- Valid To
 
- Type
 

 
Examples of invalid attributes:
 
 
- Price
 
- Inventory
 
- VIP
 
- Approved
 
- Executable
 

  
# 8. Relationship Rule
 
Relationships SHALL describe structural connectivity only.
 
Relationships SHALL NOT encode:
 
 
- permissions
 
- workflows
 
- business processes
 
- execution order
 

  
# 9. Structural Classification Rule
 
Structural Classification SHALL describe only constitutional ontology.
 
Examples:
 
 
- Subject
- Object
- Place
- Event
- Evidence
 

 
It SHALL NOT describe:
 
 
- Customer
 
- Premium
 
- Employee
 
- Dangerous
 
- VIP
 

 
Those belong to Semantic Projection.
  
# 10. Council Validation Checklist
 
Before any section of ZRM-002 is accepted, every concept must pass:
 
 
- ☐ Already authorized by ZRM-001 or this matrix.
 
- ☐ Not implementation-specific.
 
- ☐ Not mathematical.
 
- ☐ Not semantic.
 
- ☐ Not business-related.
 
- ☐ Not execution-related.
 
- ☐ Not security-related.
 
- ☐ Consistent with the constitutional primitive set (Subject, Object, Place, Event, Evidence).
 
- ☐ Not introducing a new constitutional assumption.
 
- ☐ Has exactly one constitutional owner.
 

  
# 11. Completion Rule
 
The Ontology Matrix is complete when:
 
 
- Every concept in ZRM-002 appears exactly once.
 
- Every concept has exactly one category.
 
- Every concept has exactly one constitutional owner.
 
- Every deferred concept has exactly one downstream destination.
 
- No forbidden concept appears in ZRM-002.
 

  
## Chair's recommendation
 
I would freeze this matrix **before** writing ZRM-002. It becomes the Council's "bill of materials" for the ontology. If a new concept appears during drafting that isn't in this matrix, drafting pauses and the Council decides whether to:
 
 
1. Add it to the matrix,
 
2. Defer it to another constitution, or
 
3. Reject it entirely.
 

 
This discipline prevents scope creep and keeps ZRM-002 constitutionally minimal.