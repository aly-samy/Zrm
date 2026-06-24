# ZRM v1.1
# Zyppi Reality Model
## Status
**Foundational Doctrine**
## Purpose
This document defines the permanent conceptual foundation of Zyppi.

It is intentionally independent of any database, framework, programming language, storage engine, event bus, analytics platform, graph engine, or infrastructure choice.

Technologies will change.

The reality Zyppi models must not.

The purpose of ZRM is to provide a universal representation of interactions occurring across physical and digital worlds.

Every future capability built by Zyppi—including QR codes, NFC, Smart Links, GS1 Digital Links, Product Passports, AI Agents, Attribution Systems, Commerce Flows, Identity Graphs, Analytics Platforms, and technologies not yet invented—must be expressible using this model.


## The Fundamental Belief
Most systems record events.
Zyppi records reality.
An event is a moment.
Reality is the relationship between things before, during, and after that moment.

**Traditional systems ask:**
"What happened?"

**Zyppi asks:**
`"**Who** interacted with **what**, through **which** identity, on **which** surface, for **what** purpose, under **which** circumstances, and **what** emerged afterward?"`

The answer to that question is context.
Context is the product.
Everything else is distribution.


## The Purpose of Zyppi
Zyppi exists to make previously invisible interactions visible.

- Every scan.
- Every tap.
- Every click.
- Every physical encounter.
- Every digital discovery.
- Every interaction between an actor and a referent.

The mission of Zyppi is not to move data between systems.

The mission of Zyppi is to preserve the meaning of interactions so that meaning can travel anywhere.

## The Nature of Reality
Reality consists of entities and relationships.
Entities exist.

Relationships create meaning.

A product alone has limited value.

A customer alone has limited value.

A campaign alone has limited value.

Meaning emerges when relationships connect them.

**Therefore:**
The relationship is the primary unit of intelligence.

The entity is merely the anchor point.

## The Three Layers of Reality
Reality inside Zyppi is modeled through three layers.

### Layer 1: Entities
Things that exist.
**Examples:**
- A person
- A product
- A menu
- A song
- A campaign
- A location
- A QR code
### Layer 2: Relationships
Connections between entities.
**Examples:**
- scanned
- viewed
- promoted_by
- belongs_to
- purchased
- shared
- discovered_via
### Layer 3: Facts
Assertions about entities or relationships.
**Examples:**
- when it happened
- who asserted it
- confidence level
- evidence
- source

Entities create structure.

Relationships create meaning.

Facts create trust.

Together they form reality.

## Design Goal
The ZRM must satisfy one test:
**Can every future Zyppi interaction be described using this model without introducing a new foundational primitive?**

If the answer is yes, the model is correct.

If the answer is no, the model is incomplete.

The model must be capable of representing:
- Smart Links
- QR Codes
- NFC Tags
- GS1 Digital Links
- Product Passports
- Commerce Systems
- Loyalty Programs
- AI Agents
- Physical Infrastructure
- Digital Infrastructure
- Human Actors
- Machine Actors
- Future interaction systems not yet invented without changing its foundational structure.

## The Golden Rule
Every interaction in reality can ultimately answer six questions:
1. Who?
2. What?
3. How?
4. Where?
5. Why?
6. What happened?

These six questions form the foundational ontology of Zyppi.

All future models derive from them.

No exception exists.

No feature may violate them.

No system may bypass them.

They are the bedrock of the Zyppi Reality Model.

# ZRM FOUNDATION SPECIFICATION
# Part 2 — Core Ontology (Nodes, Relationships, and Reality Rules)

## Chapter 4: The Universal Node System
Everything in Zyppi Reality Model is a Node.
A Node represents something that exists independently of a specific interaction.
Nodes persist.
Interactions come and go.
Nodes remain.

### Rule 4.1
Every node must have:

`{
  "id": "ref_01JXYZ...",
  "type": "referent",
  "created_at": "...",
  "created_by": "...",
  "valid_from": "...",
  "valid_to": null
}`

**Required properties:**

Field  | Purpose  | 
---|---
id | Immutable identifier |
type | Node category |
created_at |  When entered into graph |
created_by | Who asserted it | 
valid_from | When true in reality |
valid_to | When no longer true |


## Chapter 5: The Five Core Reality Nodes
These are the primitive building blocks of the physical-digital world.
Not because they are exhaustive.
Because they are universal.

### Node 1 — Actor
Represents the entity that initiates activity.
**Examples:**
- Anonymous visitor
- Logged-in customer
- Employee
- AI Agent
- Mobile App
- IoT Device
- POS Terminal
- System Process

 **Example**

`{
  "id": "actor_123",
  "type": "actor",
  "actor_type": "anonymous_human"
}`


#### Important Rule
Actor is not Identity.
Actor = who acted
Identity = how access occurred

**Example:**
`**Actor:**
Anonymous Visitor

**Identity:**
QR Code #17

**Referent:**
Summer Menu

**Surface:**
Table 17`


### Node 2 — Identity
Identity is the access mechanism.
Not the thing itself.
Not the content.
The access path.

**Examples**
- QR Code
- NFC Tag
- Smart Link
- GS1 Digital Link
- Deep Link
- BLE Beacon
- RFID Tag
- Future unknown identity systems

**Example**

`{
  "id": "id_7738",
  "type": "identity",
  "identity_type": "qr_code"
}`


#### Critical Principle
One Referent may have many Identities.

**Summer Menu**

├─ QR Code
├─ NFC Tag
├─ GS1 Link
└─ Smart URL

All point to same Referent.

Identity is a pointer.
Not reality.

### Node 3 — Referent
Referent is the thing being referenced.

This is one of the most important concepts in ZRM.

We intentionally avoid the word "Object".
Because objects imply physical things.

ZRM must work equally for:
- Products
- Menus
- Songs
- Videos
- Websites
- Apps
- Documents
- Buildings
- Services
- Digital Twins

**Examples**
- Spotify Song
- Restaurant Menu
- Product SKU
- PDF Brochure
- Apartment Listing
- Business Card
- Website


**Example**

`{
  "id": "ref_menu_v3",
  "type": "referent",
  "referent_type": "digital_menu",
  "name": "Summer Menu V3"
}`


#### Referent answers:
`What is this interaction actually about?`

### Node 4 — Surface
Surface is where the Identity was encountered.

This replaces the narrower concept of Location.

#### Physical Examples
- Table 17
- Shelf A3
- Billboard #5
- Product Package
- Business Card
- Conference Booth

#### Digital Examples
- Instagram Bio
- TikTok Profile
- Email Newsletter
- Website Footer
- Spotify Description
- Mobile App Screen

**Example**

`{
  "id": "surface_table17",
  "type": "surface",
  "surface_type": "physical_table"
}
`

#### Surface answers:
`Where did discovery occur?`

### Node 5 — Campaign
Campaign explains intent.
The reason an interaction exists.

**Examples**
- Summer Promotion
- Launch Campaign
- Ramadan Offer
- Album Release
- Black Friday Sale
- Influencer Partnership


**Example**

`{
  "id": "camp_2026_summer",
  "type": "campaign"
}`


#### Campaign answers:
`Why was this interaction created?`

## Chapter 6: Interaction Is Not a Node
This is a critical design decision.
Many systems model interactions as entities.
That is a mistake.

Interactions do not persist.
They happen.
Then they become facts.

Interaction is a Relationship Event.
**Example:**
`Anonymous Visitor

scanned

QR Code`

That scan is not a thing.
It is a relationship.

**Therefore:**
`Actor
   ↓
INTERACTED_WITH
   ↓
Identity`


Interaction becomes an edge.
Not a node.

## Chapter 7: Outcome Is Not a Node Same logic.
Outcome is a relationship.
Not an entity.

**Examples**
- Purchase
- Reservation
- Lead Generated
- Subscription
- Download
- Signup
- View
- Play


Outcomes link facts together.

**Example**
`Scan
   ↓
caused
   ↓
Purchase`


Purchase itself may be represented elsewhere.
But the causal relationship is the valuable part.

## Chapter 8: Reality Relationships (Edges)
Edges are first-class citizens.
This is where value lives.

**Every edge receives:**
`{
  "edge_id": "...",
  "type": "...",
  "valid_from": "...",
  "valid_to": null,
  "confidence": 0.95,
  "source": "system"
}`


### Core Relationship Types

#### ACCESSES
`Actor
  →
Identity`

**Examples:**
- Visitor scanned QR
- User tapped NFC
- Agent opened Link


#### RESOLVES_TO
`Identity
  →
Referent`

**Examples:**
- QR → Menu

- NFC → Product Passport

- Link → Song


#### DISCOVERED_ON
`Identity
  →
Surface`

**Examples:**
- QR → Table 17

- Link → Instagram Bio

- NFC → Product Package


#### ATTRIBUTED_TO
Interaction
  →
Campaign

Scan belongs to Summer Promotion


#### CAUSED
Interaction
  →
Outcome

**Examples**:
Scan → Reservation

Tap → Purchase

Link Click → Stream


#### IS_PART_OF
The most important hierarchy edge.

**Examples**:
Table 17
   →
Restaurant

Restaurant
   →
Brand

Brand
   →
Group


Or
Song
   →
Album

Album
   →
Artist


No parent_id trees.
Everything is graph-based.

## Chapter 9: The Golden Query
Every useful business question reduces to:
1. WHO
2. did WHAT
3. using WHICH identity
4. to access WHICH referent
5. from WHICH surface
6. under WHICH campaign
7. resulting in WHICH outcome
8. at WHAT time
9. with WHAT confidence

**This is the fundamental query of ZRM.
Everything else is a variation.**

## Chapter 10: Why This Ontology Survives 20 Years
Because it does not depend on:
- QR codes
- NFC
- GS1
- Marketing
- AI
- Webhooks
- Analytics
Those are implementations.
The ontology models reality itself.
**New technologies simply become:**
New Identity Types

New Referent Types

New Surface Types

New Relationship Types

The foundation remains unchanged.


# ZRM FOUNDATION SPECIFICATION
# Part 3 — Canonical Context Envelope & Reality Capture Layer

## Chapter 11: The Canonical Context Envelope
The Canonical Context Envelope (CCE) is the universal language of Zyppi.
Everything entering the Reality Model must first become a Canonical Context Envelope.
Everything leaving the Reality Model must originate from a Canonical Context Envelope.
It is the border crossing between:
`Physical Reality
        ↓
Zyppi Reality Model
        ↓
Destination Systems`

**Without the envelope:**
- QR scans
- NFC taps
- Smart links
- GS1 links
- API events
- AI actions

all become incompatible silos.
**With the envelope:**
everything speaks the same language.

### Rule 11.1
The Envelope Must Be Destination-Agnostic
Never design the envelope around:
- GA4
- Meta
- HubSpot
- Shopify
- Salesforce
- Webhooks
Those are adapters.
Adapters do not define reality.
Reality defines adapters.

### Rule 11.2
Every Envelope Represents One Fact
Not a session.
Not a profile.
Not a report.
A fact.
**Example:**
Visitor scanned QR code.

One fact.

## Chapter 12: The Structure of Reality
Every envelope contains exactly four layers.
**LAYER 1**
_Reality Fact_

**LAYER 2**
_Context_

**LAYER 3**
_Trust_

**LAYER 4**
_Time_


### Layer 1 — Reality Fact
The thing that happened.
**Example:**
`{
  "interaction_type": "qr_scan"
}`

#### Examples:
- qr_scan
- nfc_tap
- link_click
- page_view
- purchase
- signup
- reservation
- download
- stream
- share


### Layer 2 — Context
The meaning surrounding the fact.
This is where ZRM creates value.

**Context contains:**
`{
  "actor": {},
  "identity": {},
  "referent": {},
  "surface": {},
  "campaign": {}
}`


**Without Context**
qr_scan

Worth almost nothing.

**With Context**
Anonymous visitor

scanned

Menu QR

on Table 17

during Summer Campaign

at Cairo Branch

Valuable.

### Layer 3 — Trust
How certain are we?
Who asserted it?
Can we prove it?

**Example**
`{
  "source": "ios_safari",
  "confidence": 0.92,
  "verification": "deterministic"
}`


#### Trust determines:
- automation
- rewards
- attribution
- compliance

### Layer 4 — Time
When reality happened.
When Zyppi learned about it.
These are different.

## Chapter 13: Bitemporal Reality
**Most systems use:**
`{
  "timestamp": "..."
}`

This is wrong.
Reality requires two clocks.

### Clock 1: Valid Time
When the event happened.
**Example:**
User scans QR at 12:00


`{
  "valid_time": "2026-06-13T12:00:00Z"
}`


### Clock 2: System Time
When Zyppi learned it happened.
**Example:**
User was offline.

Phone syncs at 15:00.


`{
  "system_time": "2026-06-13T15:00:00Z"
}`


### Why This Matters
**Without Bitemporality:**
**Reality:**
12:00

**Database:**
15:00

Analytics becomes false.

**With Bitemporality:**
**Reality:**
12:00

**Recorded:**
15:00

Truth preserved.

### Rule 13.1
Every fact must contain:
`{
  "valid_time": "...",
  "system_time": "..."
}`

No exceptions.

## Chapter 14: Provenance
Reality is not equally trustworthy.
Some facts are proven.
Some are inferred.
Some are guessed.

Every fact must declare its origin.

**Example**
`{
  "source": "qr_scanner",
  "method": "optical_scan"
}`


**Provenance Fields**
`{
  "source": "...",
  "method": "...",
  "asserted_by": "...",
  "evidence": "..."
}`


### Examples
NFC Signature

GPS

Browser

User Login

Webhook

AI Agent

Human Operator


## Chapter 15: Confidence
Not all facts deserve equal trust.

Confidence is mandatory.
Range:
0.0 → 1.0


### Confidence Scale

 **Score** | **Meaning**
---|---
1.0 | Cryptographically proven
0.9 | Deterministic
0.7 | Strong inference
0.5 | Probable
0.3 | Weak inference
0.1 | Speculative


**Examples**
Signed NFC Tap
1.0

Logged-in User Click
0.95

Browser Fingerprint Match
0.60

AI Prediction
0.40


### Rule 15.1
Confidence is attached to facts.
Not people.
Not entities.
Facts.

## Chapter 16: The Canonical Envelope Schema
### Minimum Envelope
`{
  "event_id": "evt_01JXYZ",
  "interaction_type": "qr_scan",

  "valid_time": "2026-06-13T12:00:00Z",
  "system_time": "2026-06-13T12:00:02Z",

  "actor": {},
  "identity": {},
  "referent": {},
  "surface": {},
  "campaign": {},

  "provenance": {},
  "confidence": 0.92
}`


This schema must remain stable for years.
New capabilities extend it.
Never break it.

## Chapter 17: JSON-LD Adoption
The Canonical Envelope is JSON.
The Reality Graph is JSON-LD.
These are different concerns.

**Internal systems may operate using:**
`{
  "event_id": "...",
  "actor": {}
}`


**But semantic export should become:**
{
  "@context": {},
  "@type": "Interaction",
  "@id": "..."
}


### Reason:
JSON-LD enables:
Semantic Web
AI Agents
GS1 Compatibility
Knowledge Graph Interoperability

### Rule 17.1
**ZRM Internal Representation:**
Canonical JSON


**ZRM External Semantic Representation:**
JSON-LD


This avoids forcing every engineer to work directly with RDF-style structures while preserving future interoperability.

## Chapter 18: Reality Capture Pipeline
Reality enters Zyppi in five stages.

### Stage 1
- Capture
- QR
- NFC
- Link
- API
- Webhook


### Stage 2
- Normalize
- Convert source format into Canonical Envelope.

### Stage 3
- Validate
**Check:**
`Schema
Identity
Trust
Time
Version`


### Stage 4
Persist
Write immutable fact.

### Stage 5
Project
Convert fact into graph relationships.

## Chapter 19: The Prime Directive
Capture First.
Understand Later.

**Wrong:**
`Scan occurs

↓

Query database

↓

Resolve graph

↓

Build analytics

↓

Store event`

Slow.
Fragile.
Expensive.

**Correct:**
`Scan occurs

↓

Store fact immediately

↓

Resolve meaning asynchronously`

Fast.
Scalable.
Future-proof.

## Chapter 20: Why the Envelope Is the Product
Most platforms store events.
Zyppi stores reality.
Events are temporary.
Context survives.
Relationships compound.
Meaning accumulates.

The Canonical Context Envelope is the smallest unit of preserved reality.
Everything else in Zyppi is derived from it.

# ZRM FOUNDATION SPECIFICATION
# Part 4 — Semantic Projection Engine & Reality Graph Architecture

## Chapter 21: The Great Separation
The biggest mistake in graph architectures is attempting to make one system do everything.
It cannot.
Reality capture and reality understanding are fundamentally different workloads.

**Reality Capture requires:**
- Speed
- Reliability
- Scale
- Low Latency


**Reality Understanding requires:**
- Relationships
- Traversal
- Reasoning
- History
- Inference


These concerns must never be mixed.

### Rule 21.1
Capture Layer never performs graph traversal.
Graph Layer never participates in routing.

The redirect path remains sacred.
Nothing may compromise it.

## Chapter 22: The Semantic Projection Engine
The Semantic Projection Engine (SPE) is the brain of ZRM.
Its purpose is simple:
`Facts
  ↓
Meaning`


Input:
`Canonical Context Envelopes`
Output:
`Reality Graph`

The SPE never creates facts.
Facts already exist.
The SPE only interprets them.

**Example**
`Input:
{
  "interaction_type": "qr_scan",
  "identity": "qr_17",
  "referent": "menu_v3",
  "surface": "table_17"
}`

`
Output:
Actor
  ── ACCESSED ──► Identity

Identity
  ── RESOLVES_TO ──► Referent

Identity
  ── DISCOVERED_ON ──► Surface`


Meaning emerges.

## Chapter 23: Materialized Reality
Reality Graph is not the source of truth.
The Event Ledger is.

The graph is a projection.
A materialized interpretation.

### Rule:
Ledger = Truth

Graph = Derived


If the graph is corrupted:
Delete Graph

Replay Ledger

Rebuild Reality


Nothing is lost.

## Chapter 24: Event Sourcing Rules
Every reality fact becomes immutable.

**Wrong:**
UPDATE interaction
SET campaign='Summer'


**Correct:**
Fact 1:
Campaign = Spring

Fact 2:
Campaign = Summer


Reality evolves.
Facts remain.

### Rule 24.1
No destructive updates.
Ever.

### Rule 24.2
Facts may expire.
Facts may never be erased.

`Expiration:
{
  "valid_from": "...",
  "valid_to": "..."
}`


**Deletion is represented as:**
`{
  "event_type": "retracted"
}`


History survives.

## Chapter 25: Graph Materialization
The SPE creates two categories:

### Nodes
- Actor
- Identity
- Referent
- Surface
- Campaign


### Edges
- ACCESSED
- RESOLVES_TO
- DISCOVERED_ON
- ATTRIBUTED_TO
- CAUSED
- IS_PART_OF
- OWNS
- BELONGS_TO
- GENERATED
- LOCATED_AT


**Everything in ZRM becomes:**
Node
or
Edge


Nothing else exists.

## Chapter 26: Reality Is A Graph
Traditional databases answer:
- What happened?

Graphs answer:
- How is everything connected?


**Example:**
Restaurant asks:
`Which campaign generated
the most reservations
from QR scans
on outdoor tables
during Ramadan?`


SQL becomes painful.
Graph becomes natural.

**Traversal:**
`Campaign
 ↓
Interaction
 ↓
QR
 ↓
Table
 ↓
Reservation`


## Chapter 27: Hierarchies
Reality contains hierarchy everywhere.

**Examples:**
Table
 → Restaurant
 → Brand
 → Group


Song
 → Album
 → Artist


SKU
 → Product
 → Brand
 → Manufacturer


Never model hierarchy using:
parent_id

as a core truth.

Model hierarchy using edges.

**Example:**
Table17

IS_PART_OF

RestaurantA


**This allows:**
- Multiple parents
- Temporary structures
- Future relationships

## Chapter 28: Knowledge Emergence
Most systems store answers.
ZRM stores relationships.
Answers emerge later.

**Example:**
Nobody stores:
Best Performing Table


Instead:
Table
 ↓
Scans
 ↓
Reservations
 ↓
Revenue


The answer emerges from graph traversal.

This is why relationships are more valuable than reports.

## Chapter 29: Time Travel Queries
Because all facts are immutable:
ZRM can answer:
What did we know
on June 13, 2026?


**Example:**
AS OF 2026-06-13


Graph reconstructed.

- Campaigns
- Relationships
- Surfaces
- Identities
- All restored.

**This becomes critical for:**
- Compliance
- Audits
- Investigations
- AI Reasoning

## Chapter 30: Historical Replay
Because the ledger is immutable:
Reality can be replayed.

**Example:**
2026
You add:
BLE Beacons


Those did not exist previously.

No problem.
Replay 5 years of events.
Generate new projections.

New knowledge appears from old facts.

This is one of the most valuable properties of ZRM.

## Chapter 31: CQRS
Command Query Responsibility Segregation

**Write Model:**
Capture Facts


**Read Model:**
Answer Questions


Never mix them.

### Write Side
Optimized For:
- Speed
- Reliability
- Scale


### Read Side
Optimized For:
- Relationships
- Analytics
- Inference


This separation enables infinite growth.

## Chapter 32: Graph Governance
Reality Models fail when teams invent relationships freely.

**Bad:**
- LIKES
- PREFERS
- LOVES
- USES
- TOUCHES
- SEES
- LOOKS_AT


Thousands appear.
Chaos follows.

ZRM requires controlled vocabulary.

**Relationship types must be:**
- Explicit
- Documented
- Versioned
- Approved


Ontology before implementation.
Always.

## Chapter 33: Schema Evolution
Reality evolves.
Schemas evolve.
Foundations must survive.

### Rule:
Additive Change Only.

### Allowed:
New Node Types

New Edge Types

New Attributes


### Forbidden:
Rename Core Nodes

Delete Core Relationships

Break Existing Meaning


Backward compatibility is mandatory.

## Chapter 34: Graph Confidence Propagation
Relationships possess confidence.
Queries inherit confidence.

**Example:**
Scan
0.95

Purchase Attribution
0.80

Revenue Attribution
0.76


Confidence compounds.

AI agents must always know:
How certain is this conclusion?


Every graph answer carries confidence.

## Chapter 35: Projection Layers
Reality Graph is not one graph.
It is multiple projections.

Operational Projection
Recent Activity
Live Interactions


Analytical Projection
Campaign Analysis
Attribution
Funnels


AI Projection
Knowledge Retrieval
Reasoning
Recommendations


Compliance Projection
Audit Trails
Historical State


Same facts.
Different views.

## Chapter 36: Reality Before Analytics
Analytics is not the product.
Reality is.

**Analytics answers:**
What happened?


**Reality Graph answers:**
- Why?

- Where?

- How?

- What changed?

- What caused it?

- What is connected?


Analytics becomes a projection of reality.
Not the source of reality.

## Chapter 37: The ZRM Engine
The complete architecture:
Physical Reality
        ↓

Capture Layer

(QR / NFC / Link / API)

        ↓

Canonical Context Envelope

        ↓

Immutable Event Ledger

        ↓

Semantic Projection Engine

        ↓

Reality Graph

        ↓

Projections

        ├─ Analytics
        ├─ AI
        ├─ Compliance
        ├─ Attribution
        └─ Automation

        ↓

Adapters

GA4
Meta
HubSpot
Salesforce
Webhooks
GS1
Future Systems


## Chapter 38: The Second Prime Directive
Never store reports.
Store reality.
Never store conclusions.
Store relationships.
Never optimize for today's query.
Preserve tomorrow's knowledge.

The Semantic Projection Engine exists for one reason:
To convert immutable facts
into reusable meaning.

That meaning becomes the foundation upon which every future Zyppi capability is built.

# PART 5 — THE CANONICAL CONTEXT ENVELOPE (CCE)
This section defines the single most important artifact in the entire Zyppi Reality Model.
Everything before this document defines reality.
The Canonical Context Envelope defines how reality is transmitted.
Every scan. Every tap. Every click. Every AI interaction. Every future GS1 Digital Link. Every future Product Passport.
Will eventually become a Canonical Context Envelope.

## 5.1 The Core Principle
The Canonical Context Envelope (CCE) is the universal transport format of Zyppi.
It exists to answer one question:
"What happened, to what, where, why, and with what confidence?"
### The CCE is:
- Destination-agnostic
- Future-proof
- Graph-compatible
- AI-readable
- Human-readable
- Machine-verifiable
- Every adapter consumes the same envelope.
- GA4.
- Meta.
- HubSpot.
- Salesforce.
- Webhooks.
- AI Agents.
- Future systems.

Everything receives the same truth.
Only the translation changes.
Never the source.

## 5.2 Design Principles
The envelope must satisfy seven principles.
### Principle 1 — Complete
The envelope must contain enough information to reconstruct meaning without additional lookups.
`Bad:
{
  "event": "qr_scan",
  "link_id": "123"
}`

`Good:
{
  "interaction_type": "qr_scan",
  "identity": {...},
  "surface": {...},
  "referent": {...}
}`


### Principle 2 — Immutable
Once emitted:
The envelope never changes.
Corrections create new envelopes.
Never mutate history.

### Principle 3 — Self-Describing
An AI agent should understand the envelope without custom documentation.
Every field should have explicit meaning.

### Principle 4 — Globally Identifiable
Every major object contains:
"id": "urn:zyppi:..."

No local identifiers.
No ambiguous references.

### Principle 5 — Bitemporal
Every envelope contains:
valid_time
system_time

Reality time.
Recorded time.

### Principle 6 — Provenance Aware
Every assertion must include confidence.
The system must know how trustworthy information is.

### Principle 7 — Adapter Independent
The envelope never changes because a destination changes.
Never design around GA4.
Never design around Meta.
Never design around today's integrations.

## 5.3 Envelope Structure
The envelope has 10 sections.
Envelope
│
├── Metadata
├── Interaction
├── Actor
├── Identity
├── Surface
├── Referent
├── Campaign
├── Outcome
├── Provenance
└── Extensions


## 5.4 Metadata Section
**Purpose:**
Technical envelope information.
Example:
`{
  "metadata": {
    "envelope_version": "1.0",
    "workspace_id": "urn:zyppi:workspace:abc",
    "interaction_id": "urn:zyppi:interaction:xyz",
    "generated_at": "2027-05-10T14:00:00Z"
  }
}`

**Rules:**
Required
Immutable
Never business-facing

## 5.5 Interaction Section
Represents the event occurring in reality.
**Example:**
`{
  "interaction": {
    "type": "qr_scan",
    "valid_time": "2027-05-10T13:59:55Z",
    "system_time": "2027-05-10T14:00:00Z"
  }
}
`
### Possible values:
- qr_scan
- nfc_tap
- smart_link_click
- page_view
- conversion
- purchase
- reservation
- form_submit
- app_open
- video_play
- ai_query
- custom

Interaction is the center of the envelope.
Everything else provides context.

## 5.6 Actor Section
Represents who initiated the interaction.
Important:
Actor is not identity stitching.
Actor describes the participant.
Not the person.
**Example:**
`{
  "actor": {
    "id": "urn:zyppi:actor:anon123",
    "type": "anonymous_human"
  }
}
`
### Possible types:
- anonymous_human
- known_customer
- employee
- organization
- device
- ai_agent
- system

Future systems may enrich Actor.
The original interaction remains immutable.

## 5.7 Identity Section
Represents how the interaction entered the system.
Identity is an access method.
Not the thing itself.
**Example:**
`{
  "identity": {
    "id": "urn:zyppi:identity:qr_001",
    "type": "qr_code"
  }
}`

### Possible types:
- qr_code
- nfc_tag
- smart_link
- deep_link
- gs1_digital_link
- barcode
- rfid
- beacon
- api_endpoint

One Referent may have many Identities.

## 5.8 Surface Section
Represents where the identity was encountered.
Physical or digital.
**Examples:**
`Restaurant:
{
  "surface": {
    "type": "table",
    "name": "Table 17"
  }
}
`
`Digital:
{
  "surface": {
    "type": "instagram_bio",
    "name": "Artist Bio Link"
  }
}`

### Possible values:
- table
- shelf
- package
- poster
- flyer
- billboard
- event_booth
- instagram_bio
- tiktok_profile
- youtube_description
- email
- website
- mobile_app

Surface is discovery context.

## 5.9 Referent Section
Represents what the interaction is actually about.
This is the most important business entity.
**Examples:**
- song
- album
- artist
- menu
- product
- landing_page
- service
- event
- store
- brand
- digital_twin
- product_passport

**Example:**
`{
  "referent": {
    "id": "urn:zyppi:referent:menu_v3",
    "type": "restaurant_menu",
    "name": "Summer Menu V3"
  }
}`

Identity points to Referent.
Referent owns meaning.

## 5.10 Campaign Section
Represents intentional business context.
**Example:**
`{
  "campaign": {
    "id": "urn:zyppi:campaign:summer2027",
    "name": "Summer Promotion"
  }
}`

### Campaigns answer:
- Why did this interaction exist?
Not all interactions require campaigns.
Campaign is optional.

## 5.11 Outcome Section
Represents value creation.
**Without Outcome:**
Interactions are activity.
**With Outcome:**
Interactions become business intelligence.
**Example:**
`{
  "outcome": {
    "type": "reservation_created",
    "value": 4,
    "unit": "people"
  }
}`

**Examples:**
- purchase
- reservation
- signup
- lead
- app_install
- subscription
- video_completion
- coupon_redeemed

Outcomes may occur seconds or months later.

## 5.12 Provenance Section
One of the most important sections.
**Represents:**
- How much should we trust this?
**Example:**
`{
  "provenance": {
    "source": "ios_camera",
    "method": "optical_scan",
    "confidence": 0.85
  }
}`

### Confidence levels:

Level  | Meaning
---|---
1.0  | Cryptographically proven |
0.9 | Deterministic |
0.7| Strong inference | 
0.5 | Weak inference |
0.3 | AI hypothesis | 

Future automation can use this directly.
### Example:
- Issue reward only if confidence >= 0.9


## 5.13 Extensions Section
The future-proofing layer.
Every future feature lives here.
**Example:**
`{
  "extensions": {
    "weather": {
      "temperature": 32
    },
    "gs1": {
      "batch": "A102"
    }
  }
}
`
### Rules:
- Never pollute core schema.
- New industries extend here.
- Core model remains stable forever.

## 5.14 The Golden Rule
Every Canonical Context Envelope must answer:
- WHO initiated it?
- WHAT was it about?
- HOW was it accessed?
- WHERE was it discovered?
- WHY did it exist?
- WHEN did it happen?
- WHAT VALUE was created?
- HOW CERTAIN are we?

If an envelope cannot answer these questions,
it is incomplete.

# PART 6 — THE REALITY GRAPH
The Canonical Context Envelope captures reality.
The Reality Graph understands reality.
This is the layer that transforms Zyppi from a platform that records interactions into a system that understands relationships.
**Without the Reality Graph:**
`QR Scan → Event → Analytics`

**With the Reality Graph:**
`Actor
  │
  ├─ scanned
  │
Identity
  │
  ├─ resolves_to
  │
Referent
  │
  ├─ promoted_by
  │
Campaign
  │
  ├─ generated
  │
Outcome`

The difference is not storage.
The difference is meaning.

## 6.1 The Purpose of the Reality Graph
The Reality Graph exists to answer questions that event systems cannot answer.
**Event systems answer:**
- What happened?
**Reality Graphs answer:**
- Why did it happen?
- What caused it?
- What is connected to it?
- What changed because of it?
- What is likely to happen next?

## 6.2 The Core Philosophy
Everything in reality becomes one of two things:
### Nodes
Persistent entities.
**Examples:**
- Actor
- Referent
- Identity
- Surface
- Campaign
- Outcome
- Organization
- Location
- Product
- Venue
- Brand
- Store


### Relationships
Connections between entities.
**Examples:**
- SCANNED
- VIEWED
- PROMOTED_BY
- PART_OF
- LOCATED_AT
- OWNS
- GENERATED
- PURCHASED
- CLICKED
- DISCOVERED_VIA


The graph stores both.
Nodes without relationships are meaningless.
Relationships without nodes are impossible.
Meaning emerges from both.

## 6.3 The Fundamental Rule
The graph never stores duplicated truth.
Store facts once.
Reference everywhere.
**Bad:**
Table 17
Restaurant A

Table 17
Restaurant A

Table 17
Restaurant A

**Good:**
Table17
   │
   └─ PART_OF
         │
         ▼
RestaurantA

Every interaction references the same node.

## 6.4 Graph Layers
The Reality Graph contains five layers.
`Reality Graph
│
├── Entity Layer
├── Relationship Layer
├── Temporal Layer
├── Provenance Layer
└── Semantic Layer`


## 6.5 Entity Layer
The Entity Layer contains persistent things.
### Core entities:
- Actor
- Identity
- Surface
- Referent
- Campaign
- Outcome
- Organization


**Example:**
Actor
 └── Anonymous Human

Identity
 └── QR Code #118

Surface
 └── Table 17

Referent
 └── Summer Menu V3

Campaign
 └── Summer 2027

Outcome
 └── Reservation


Entities can exist without interactions.
A menu exists before a scan.
A QR code exists before being scanned.
A campaign exists before generating results.

## 6.6 Relationship Layer
Relationships are first-class citizens.
This is critical.
Most databases treat relationships as implementation details.
ZRM treats relationships as knowledge.

**Example:**
Actor
   │
   └── SCANNED
             │
             ▼
          Identity


### Relationship example:
`{
  "relationship_id": "urn:zyppi:rel:123",
  "type": "SCANNED"
}
`
Relationships have identities.
Relationships are queryable.
Relationships are auditable.
Relationships are immutable.

## 6.7 Core Relationship Types
### Interaction Relationships
- SCANNED
- TAPPED
- CLICKED
- VIEWED
- OPENED
- SHARED
- DOWNLOADED
- SUBMITTED


### Structural Relationships
- PART_OF
- LOCATED_AT
- BELONGS_TO
- OWNS
- CONTAINS


### Attribution Relationships
- PROMOTED_BY
- ATTRIBUTED_TO
- DISCOVERED_VIA
- INFLUENCED_BY


### Outcome Relationships
- GENERATED
- RESULTED_IN
- PURCHASED
- RESERVED
- CONVERTED_TO


### Identity Relationships
- RESOLVES_TO
- ALIASES
- DERIVED_FROM
- REPRESENTS


## 6.8 Identity Resolution
One of the most important graph capabilities.
**Example:**
`QR Code #1
NFC Tag #1
GS1 Link #1

      │
      ▼

Product Passport`

**Graph:**
`Identity
  └─ RESOLVES_TO
        Referent
`
Multiple identities.
One referent.
Infinite access methods.
Single source of truth.

## 6.9 Surface Hierarchies
Physical reality is hierarchical.
**Example:**
Table 17
   │
   ▼
Restaurant
   │
   ▼
Branch
   │
   ▼
Brand

**Graph:**
Table17
  PART_OF RestaurantA

RestaurantA
  PART_OF CairoBranch

CairoBranch
  PART_OF CrimsonFoods


**Digital hierarchy:**
Instagram Bio
   │
   ▼
Instagram Profile
   │
   ▼
Artist Brand

Same graph.
Different reality.

## 6.10 Referent Hierarchies
Referents also have structure.
**Example:**
Song
 └─ PART_OF Album

Album
 └─ PART_OF Artist

Artist
 └─ PART_OF Label

**Or:**
SKU
 └─ PART_OF Product

Product
 └─ PART_OF Brand

Graph handles both equally.

## 6.11 Temporal Layer
Reality changes.
The graph must preserve history.
Never overwrite.
Never destroy.
Never mutate truth.

**Every node:**
`{
  "valid_from": "...",
  "valid_to": null
}`


**Every relationship:**
`{
  "valid_from": "...",
  "valid_to": null
}`


**Example:**
Menu V2
valid_to = June 1

Menu V3
valid_from = June 1

Both remain in history.

## 6.12 Bitemporal Graph
Every fact has two clocks.
### Valid Time
When reality happened.
`Customer scanned menu at 12:00`


### System Time
When Zyppi learned about it.
`Phone synced at 15:00`


Graph stores both.
**Example:**
`{
  "valid_time": "12:00",
  "system_time": "15:00"
}
`
**This enables:**
- Time travel
- Auditability
- Delayed sync
- Offline interactions

## 6.13 Provenance Layer
Every node and relationship must answer:
- Why should I trust this?

**Example:**
`{
  "source": "nfc_chip",
  "confidence": 1.0
}`


**Or:**
`{
  "source": "browser_fingerprint",
  "confidence": 0.65
}`


Confidence is stored directly on graph relationships.
**Example:**
Actor
   │
   └─ SCANNED
      confidence=0.95


## 6.14 Semantic Layer
The semantic layer makes the graph AI-native.
Every relationship carries meaning.
Not just IDs.
Not just foreign keys.
Meaning.

**Example:**
`Actor
  DISCOVERED_VIA
Surface`

`Surface
  PROMOTED
Referent`

`Referent
  GENERATED
Outcome`

An AI can understand this chain naturally.

## 6.15 Reality Queries
The graph exists to answer questions.
**Examples:**

### Query 1
- Which tables generated the most reservations?
Surface
 → GENERATED
Outcome


### Query 2
- Which campaigns influenced purchases?
Campaign
 → INFLUENCED
Outcome


### Query 3
- Which identities resolve to the same product?
Identity
 → RESOLVES_TO
Referent


### Query 4
- How did users discover this song?
Actor
 → DISCOVERED_VIA
Surface
 → PROMOTED
Referent


### Query 5
- What chain of interactions led to a purchase?
Actor
 → Interaction
 → Referent
 → Outcome


## 6.16 The AI Layer
The Reality Graph is not designed only for dashboards.
It is designed for agents.
Future AI systems should be able to ask:
- What physical surfaces drive purchases?
- What campaigns influence repeat visits?
- Which products are most discovered via NFC?
- What identities are underperforming?
- What locations produce the highest value outcomes?

Without custom code.
Without hardcoded reports.
Without new schema.
The graph already contains the answer.

## 6.17 The Ultimate Principle
Events disappear.
Relationships compound.
A QR scan is valuable for seconds.
The relationship created by that scan may be valuable for decades.
The purpose of the Reality Graph is not to remember events.
The purpose of the Reality Graph is to preserve meaning.

# ZRM FOUNDATION DOCUMENT — PART 7
# Evolution, Governance, Interoperability & 10-Year Strategy
_This final section defines how the Zyppi Reality Model (ZRM) survives technology shifts, new business models, AI evolution, and future physical identity standards.
A data model is only foundational if it can evolve without breaking reality._

## 7.1 The Prime Directive
Every future Zyppi capability must be expressible as:
`Nodes + Relationships + Facts + Time`
If a future feature cannot be represented using those primitives, the model is wrong.
Never build special-purpose structures before asking:
- Can this be represented inside the Reality Graph?
**Examples:**

Future Feature  | Representation
---|---
NFC Passport  | Identity → Referent
GS1 Digital Link | Identity → Referent
BLE Beacon | Identity → Surface
Digital Twin | Referent
AI Agent | Actor
Customer Journey | Relationship Chain
Product Ownership | Relationship
Loyalty Program | Relationship
Membership | Relationship
Physical Asset Tracking | Relationship Graph

Everything becomes graph-compatible.

## 7.2 The ZRM Stability Promise
Once a node type or relationship enters the public schema:
**It can be:**
- Extended
- Deprecated
- Replaced
But never silently changed.
**This guarantees:**
- backward compatibility
- adapter stability
- ecosystem trust

**Allowed**
`{
  "actor": {
    "type": "human",
    "language": "en"
  }
}`

**Later:**
`{
  "actor": {
    "type": "human",
    "language": "en",
    "timezone": "UTC"
  }
}`

New fields added.
No breakage.

**Forbidden**
Today:
"type": "human"

Tomorrow:
"type": {
   "name":"human"
}

This breaks consumers.
Not allowed.

## 7.3 Schema Versioning
Every envelope carries a schema version.
`{
  "zrm_version": "1.0"
}
`
**Examples:**
1.0
1.1
1.2
2.0

### Rules:
**Minor Version**
Adds fields.
Backward compatible.
1.0 -> 1.1


**Major Version**
Changes semantics.
1.x -> 2.x

Requires migration strategy.

## 7.4 Reality Graph Governance
The graph becomes a critical asset.
Therefore:
No team may create new node types casually.
New node types require governance review.

**Good**
- Actor
- Referent
- Identity
- Surface
- Campaign
- Interaction
- Outcome


**Bad**
- SuperCampaign
- MegaCampaign
- CampaignPlus
- MarketingCampaign

Semantic duplication creates chaos.

### Every new node must answer:
- Why isn't this an attribute?
**Example:**
Color

Not a node.
Attribute.

- Why isn't this a relationship?
**Example:**
Ownership

Not a node.
Relationship.

- Why must it be a node?
**Example:**
Organization

Independent lifecycle.
Multiple relationships.
**Therefore:**
Node.

## 7.5 The Reality Query Language
Every useful business question should become graph traversals.

### Marketing
**Question:**
- Which campaign produced the highest purchase rate?
**Traversal:**
Campaign
→ Interaction
→ Outcome


### Retail
**Question:**
- Which packaging version drives more scans?
**Traversal:**
Referent
→ Identity
→ Interaction


### Music
**Question:**
- Which traffic source drives Spotify saves?
**Traversal:**
Surface
→ Interaction
→ Outcome


### AI
**Question:**
- What does this product represent?
**Traversal:**
Referent
→ Parent Referents
→ Campaigns
→ Outcomes


The graph becomes the query engine of reality.

## 7.6 AI-Native Design
Most software today is user-native.
ZRM must be AI-native.
**Meaning:**
An AI agent should understand reality without custom prompts.

**Every node should expose:**
`{
  "id":"",
  "type":"",
  "name":"",
  "description":""
}`


**Every relationship should expose:**
`{
  "relationship_type":"",
  "source":"",
  "target":"",
  "confidence":1.0
}`


**Future AI systems should be able to:**
- traverse
- infer
- summarize
- reason
without Zyppi-specific logic.

## 7.7 GS1 Compatibility Strategy
Helios and future product passports require compatibility with GS1.
ZRM should not become GS1.
ZRM should map to GS1.
Important distinction.

### ZRM remains:
Universal

### GS1 remains:
Supply-chain specific


### Mapping Layer:
ZRM Referent
      ↓
GS1 Product

ZRM Identity
      ↓
GS1 Digital Link

ZRM Interaction
      ↓
GS1 EPCIS Event


**This allows:**
- retail
- marketing
- logistics
- product passports
to coexist.

## 7.8 Digital Twin Readiness
Every physical object should eventually have a digital representation.
ZRM already supports this.
**Example:**
Physical Product
        ↓
Referent


**Future attributes:**
`{
  "serial_number":"",
  "manufactured_at":"",
  "batch":"",
  "owner":""
}`


No redesign required.
The foundation already supports digital twins.

## 7.9 The 100 Million Interaction Test
**Assume:**
- 100M interactions
- 10M identities
- 5M surfaces
- 2M referents

The model must still work.

**This means:**
### Writes
Append-only.
Never update history.

### Reads
Projection-driven.
Never query raw event streams.

### Graph
Optimized for traversal.
Not ingestion.

### Analytics
Materialized.
Not reconstructed per request.

This separation allows infinite scale.

## 7.10 The 10-Year North Star
**Today Zyppi tracks:**
- QR scans
- Smart links
- NFC taps

**Tomorrow it may track:**
- GS1 Digital Links
- Product Passports
- BLE interactions
- AI agent actions
- AR experiences
- IoT devices
- Ownership transfers
- Physical assets

The foundation must not care.
**Because all reality ultimately reduces to:**
1. Something
2. interacted with
3. something else
4. somewhere
5. for some reason
6. at some time
7. with some outcome


## Final ZRM Axiom
The Zyppi Reality Model is not an analytics schema.
It is not an event schema.
It is not a webhook payload.
It is not a QR platform data model.

It is a durable representation of reality that allows physical and digital interactions to be captured, understood, traversed, attributed, and distributed without losing meaning.

Everything else—GA4, Meta, webhooks, dashboards, AI agents, GS1, Helios, NFC, product passports—is merely a projection of that reality.



# Part 8 — ZRM v1.1 Addendum (Clarifications & Hardening)

The key principle should be:

> This addendum does not alter the ontology, laws, primitives, or architectural foundations of ZRM v1.

It clarifies implementation ambiguities discovered during architectural review and provides additional guidance for scalability, interoperability, and long-term durability.



This keeps the Stability Promise intact.


---

**The addendum should contain exactly eight sections:**

## 8.1 Interaction Clarification

Clarify the distinction between:

- Interaction as an immutable captured fact
- Interaction as graph relationships during projection


This resolves the ledger-vs-graph ambiguity.


---

## 8.2 Law 11 — Idempotency

Define duplicate handling.

### Law 11:
> The Same Fact Must Produce The Same Reality

Every Interaction must possess a globally unique interaction_id.

If the same interaction_id is received multiple times:

• The original fact remains authoritative.
• Duplicate submissions are ignored.
• Historical records are never modified.

Reality is immutable.
Duplicates are not reality.


---

## 8.3 Actor Resolution Framework

Define how anonymous actors become known actors.

**Example:**

Anonymous Actor
→ RESOLVED_AS
Known Customer

confidence: 1.0
method: authenticated_login

Identity evolves through relationships.

Actors are never mutated.


---

## 8.4 Confidence Propagation

Define default behavior.

> child_confidence =
parent_confidence × relationship_confidence

**Example:**

0.95 × 0.80 = 0.76

Relationship types may override this rule.


---

## 8.5 Conflict Preservation Framework

Define how competing facts are handled.

Fact A
confidence 1.0

Fact B
confidence 0.8

Both are preserved.

Neither is deleted.

Reality may contain disagreement.

Queries determine acceptable trust thresholds.


---

## 8.6 Schema Registry Requirement

Require machine-readable discovery.

**Registry exposes:**

- Node Types
- Relationship Types
- Version History
- Deprecation Status
- Examples


This strengthens AI-native interoperability.


---

## 8.7 Materialized Projection Guidance

Expand the existing scalability principles already present in Part 7.

**Clarify:**

- Raw facts remain immutable

- Graph remains traversable

- Analytics may use materialized projections

- Materialized projections are derived reality, not source reality


This avoids future misunderstandings.


---

## 8.8 Ownership & Authority Relationships

Introduce recommended relationship patterns:

OWNS
OPERATES
MANAGES
LICENSES

**Examples:**

Organization
→ OWNS
Referent

Organization
→ OPERATES
Surface

Organization
→ LICENSES
Identity

**This becomes extremely valuable for:**

GS1

Product Passports

Helios

Digital Twins

AI Agents


without introducing a new primitive.


---

I would explicitly avoid placing the following in the addendum:

Outcome becomes a node

Context becomes a primitive

Workspace becomes a core entity

Interaction becomes a permanent graph node

JSON-LD becomes mandatory

Authorization becomes a foundational primitive


Those are architectural directions, not hardening clarifications, and they would change the ontology rather than strengthen it.

A clean ZRM structure would then become:

Part 1–7
ZRM Constitution

Part 8
ZRM v1.1 Addendum
(Clarifications & Hardening)

Future:
Part 9
ZRM v1.2 Addendum

Future:
Part 10
ZRM v1.3 Addendum

This preserves the original document as the immutable foundation while allowing the model to mature through additive amendments, exactly the way a durable standard should evolve.

