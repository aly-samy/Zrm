# GNSR-001 — Global Naming Synchronization Report
---|---
Status: | Ratified Synchronization Document

# Purpose
This document records all naming corrections required to synchronize the constitutional corpus following the creation of CL-16 Intelligence and CL-17 Graph Core.

This document introduces no architectural changes.

# Section 1 — Constitutional Naming Authority
The following cluster names are canonical:
Cluster | Canonical Name
---|---
CL-01 | Actor
CL-02 | Surface
CL-03 | Touchpoint
CL-04 | Identity
CL-05 | Referent
CL-06 | Intent 
CL-07 | Intent Contract
CL-08 | System
CL-09 | Transaction
CL-10 | Outcome
CL-11 | Event
CL-12 | Strategic
CL-13 | Temporal
CL-14 | Compliance
CL-15 | Schema
CL-16 | Intelligence
CL-17 | Graph Core

# Section 2 — Legacy Intelligence References
All references to:
- "CL-11 Intelligence"
- "Intelligence Cluster"
- "Evidence Cluster"
shall be reviewed and synchronized.

## Replacement Rules:
**If the reference concerns:**
- interpretation
- analysis
- confidence
- prediction
- recommendation
- AI output
- inferred meaning

**Then:**
Replace with:
- CL-16 Intelligence

# Section 3 — Event Synchronization
CL-11 exclusively owns:
- Events
- Interactions
- Observations
- State changes
- Occurrences

No Intelligence object may be stored in CL-11.

# Section 4 — Transaction Correction
## WS-03A.6
### CP-TXN-05
**Current text:**
- "CL-11 Evidence"

**Corrected text:**
- "CL-16 Intelligence"

**Reason:**
Confidence scores are interpretive artifacts and therefore Intelligence objects.

# Section 5 — Campaign Synchronization
Campaign references shall be interpreted according to CA-002.

- Campaign Identity → CL-04
- Campaign Context → CL-16

No standalone Campaign Primitive exists.

# Section 6 — Completion Statement
## Following adoption of GNSR-001:
- All constitutional references to Intelligence ownership shall resolve to CL-16.
- All Event ownership shall resolve to CL-11.
The naming migration is complete.

