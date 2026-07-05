# What is Zyppi?
---
---
###### By: Aly A. Samy
###### Version: 3.0 — The Routing Layer
###### Council Synthesis Edition

---

# 1. The Shift Nobody Is Pricing In

For fifty years, a barcode answered one question:

**"What is this product?"**

GS1 Sunrise changes that question forever.

A barcode is becoming a permanent digital address. Not a lookup key for a checkout system — a place. Every product, for the first time in history, can be reached, not just recognized.

Almost nobody building for this moment is treating it as an infrastructure shift. Most are treating it as a compliance deadline: generate the digital link, tick the box, move on.

That gap is the opportunity.

---

# 2. The Problem Isn't Content. It's Fragmentation.

A single manufacturer today might have:

- `warranty.company.com`
- `manuals.company.com`
- `spareparts.company.com`
- `support.company.com`
- `recycle.company.com`
- a dealer portal, a distributor portal, an internal ERP screen, an EU-only DPP page

None of these systems know about each other. None of them know *who* is arriving — a consumer, a technician, a distributor, a regulator, an AI agent — or *why*. So every company solves this the same way: one static QR code that points to one static page, regardless of who scans it or what they actually need.

The result is friction on every side. Consumers land on the wrong page. Technicians dig through generic support content to find a service manual. Distributors get consumer-facing pages instead of wholesale portals. Compliance teams bolt DPP pages onto systems never designed to carry regulatory data.

The problem was never "products lack content." Companies already have warranty systems, manual repositories, dealer portals, ERPs. The problem is that nothing sits between the physical product and all of that — nothing that knows the context of the person standing in front of it and can send them to the right place.

That missing layer is the product.

---

# 3. What Zyppi Is

**Zyppi is the identity and routing layer for physical products.**

Every product receives one permanent digital identity. Whenever that identity is accessed — scanned, tapped, looked up — Zyppi determines the context, logs the event, and routes the person or system to the correct destination. It does not host that destination. It does not replace the systems a company already runs. It decides, in milliseconds, where each interaction should go — and remembers that it happened.

Think of it as:

| Category | Company | What it made trivial |
|---|---|---|
| Domain resolution | DNS | Turning names into addresses |
| Payments | Stripe | Accepting money without building a payment stack |
| Identity | OAuth | Proving who someone is without owning their credentials |
| Communication | Twilio | Sending a message without owning telecom infrastructure |
| **Physical products** | **Zyppi** | **Knowing where every interaction should go — without owning the destination** |

A product's QR code doesn't point to a page. It points to `zyppi.me/p/{identity}`. Zyppi evaluates who's asking, and routes:

- Consumer → warranty registration
- Technician → service manual
- Distributor → wholesale portal
- Internal employee → ERP screen
- EU consumer → Digital Product Passport view
- US customer → support center
- Expired product → recycling instructions
- Suspicious scan pattern → authenticity verification flow

Same physical QR code. Same NFC tag. Different destination, every time, based on context — and every one of those decisions is logged as a verified event against that product's permanent identity.

---

# 4. What Zyppi Is Not

**Not a QR code generator.** The QR is the doorway, not the product. Anyone can generate a static QR in five minutes; almost nobody can make it context-aware.

**Not a CMS or Digital Experience Platform.** Zyppi does not host manuals, videos, or marketing content. It routes to wherever that content already lives — or to a minimal templated destination when it doesn't exist yet (Section 6).

**Not an ERP, PLM, or CRM replacement.** Those remain the systems of record. Zyppi never asks a company to migrate data into it. It asks for destination URLs and routing rules.

**Not a Digital Product Passport vendor in the traditional sense.** Zyppi doesn't compete with DPP platforms as a hosting alternative — it resolves DPP requests to the right jurisdictional destination and, where regulation demands it, carries a thin structured record so that obligation is met even if the manufacturer's own systems go down (Section 8).

---

# 5. How It Works

```
Identity
   ↓
Context Detection      (who, where, what device, what history)
   ↓
Decision Engine         (routing rules + policies + permissions)
   ↓
Route
   ↓
Event Logged            (immutable, timestamped, attributed)
   ↓
Destination             (anywhere: SAP, Shopify, Salesforce, a PDF, a dealer app, a deep link)
```

**Step 1 — Identity.** A company uploads a product list (or connects a feed). Every SKU or serialized unit receives a permanent identity: `ZE-IDT-xxxxx` internally, exposed externally as a GS1 Digital Link, NFC payload, or QR — carrier-agnostic, format-agnostic.

**Step 2 — Routing rules.** The company defines destinations per context: "consumers go here," "technicians authenticated via X go here," "EU traffic goes to the DPP view," "unregistered scans past the expiration date go to recycling." No code. No integration. Just destination URLs and conditions.

**Step 3 — Resolution.** Every scan, tap, or API call resolves through Zyppi's decision engine in real time and is redirected — invisibly, in milliseconds — to the right place.

**Step 4 — The event ledger.** Every resolution is recorded: who (or what class of actor), when, where, which policy fired, which destination was served. This is the exhaust of routing, not its purpose — but it is the asset that compounds.

---

# 6. The Fallback Destination (Not Hosting — Configuration)

A pure router has one honest weakness: a small brand with no existing warranty system, no manual repository, and no dealer portal has nothing for Zyppi to route to. Day-one value would be invisible.

The fix is a single, templated fallback page — logo and brand color as the only configuration surface, no page builder, no CMS, no freeform content editing. It renders product identity, a manual link if one exists, a warranty registration form, and (where applicable) structured DPP fields. It is a *rendering template*, not a hosted asset library: no media storage, no arbitrary content, no per-customer infrastructure footprint beyond a row of configuration values.

This is deliberately not "hosting weight" in the way v1/v2 would have created it — there is no proliferating library of manuals, PDFs, and videos sitting on Zyppi's infrastructure. It's one template, parameterized per brand, rendering data that already exists in the routing and identity layer. The cost profile stays close to pure routing, not CMS.

This also solves the DPP problem directly. EU Digital Product Passport regulation requires certain data to remain persistently available and verifiable, independent of whether a manufacturer's own systems stay online. The templated fallback, backed by a thin structured data record (JSON-LD / schema.org, not media), satisfies that requirement without turning Zyppi into a content host. The customer's systems remain the source of truth wherever they exist; the fallback exists for the gap, and for regulatory persistence.

---

# 7. What Zyppi Stores — and What It Doesn't

**Zyppi stores:**
- Identity records (permanent, immutable)
- Routing rules and policies
- Permissions and authority boundaries
- Destination references (URLs, not content)
- The event and intent ledger (append-only, bitemporal)
- A thin structured compliance record where regulation requires persistence

**Zyppi does not store:**
- Manuals, videos, marketing content, product images
- Warranty case data, service tickets, CRM records
- Anything that belongs inside a customer's own systems of record

This boundary is the whole business model. It is also, not coincidentally, the constitutional principle this platform was already built on: *Zyppi owns truth about identity, relationships, and events — not content.* The router model isn't a pivot away from that architecture. It's the cleanest possible expression of it.

Being precise here matters for cost as much as positioning: the event ledger is not "free" at scale — it is the core value asset and it is write-heavy. It is dramatically cheaper than hosting rich media, but it is a real infrastructure line item, which is why free-tier event retention is capped (Section 9) rather than unlimited.

---

# 8. The Flywheel

The critical correction from every earlier version: people do not scan because a company wants analytics. They scan because they want something — a manual, a warranty claim, proof of authenticity, a spare part, install instructions.

```
Identity
   ↓
Permanent Address
   ↓
Real Interactions          (people already have reasons to scan)
   ↓
Events + Intent History    (the exhaust, not the ask)
   ↓
Routing Intelligence       (rules, patterns, policies accumulate)
   ↓
Enterprise Workflows       (warranty, recall, supplier recovery — as routing policies)
   ↓
Platform Compounding
```

Nobody has to be convinced to scan. Consumers already scan for manuals and authenticity. Technicians already scan for service data. Distributors already scan for inventory. Zyppi's job is only to become the destination that resolves those scans intelligently — the event history builds itself as a byproduct of utility, not as a manufactured behavior.

---

# 9. Revenue Ladder

**Free**
- Up to 250 product identities
- Templated fallback page (logo + brand color only)
- Standard routing (consumer / default)
- Last 1,000 events retained
- Zyppi branding on fallback page

**Starter** *(self-serve, no sales call)*
- Higher SKU ceiling
- Custom domain
- Context-based routing rules (device, geography, actor type)
- Full event history
- Basic API access
- DPP structured fields

**Growth** *(self-serve or lightly assisted)*
- Unlimited routing policies
- Multi-destination logic (distributor, technician, internal)
- Integrations (Shopify, common ERPs/CRMs)
- Team permissions
- Analytics on routing and intent patterns

**Enterprise** *(sales-assisted — this is where the original wedge lives)*
- Supplier warranty chargebacks
- Recall routing and automation
- Counterfeit/authenticity investigation workflows
- Field service and installation verification
- ERP-grade integration
- AI-driven routing and anomaly detection
- Compliance evidence and audit trail export

The critical difference from every prior version: warranty recovery, recall management, and supplier chargebacks are no longer separate products bolted onto identity. They are routing policies layered on an identity and intent graph that already exists by the time a company is ready to buy them. The enterprise sale gets shorter because the hard part — getting products identified and generating real event history — already happened for free.

---

# 10. The Moat

A QR generator is a weekend project. A landing page builder is a commodity. What is not replicable in a weekend is the accumulated routing intelligence tied to a company's actual products: years of context rules, permission boundaries, and an immutable intent ledger describing exactly what happened to every unit, every scan, every actor, in what context.

The switching cost is not the identifier. It's the operational intelligence built on top of it — the same dynamic that made Stripe and Twilio sticky long after "processing a payment" and "sending a text" became commodity capabilities elsewhere.

---

# 11. Distribution Without a Sales or Marketing Budget

Zyppi does not lead with GS1 or compliance language — almost nobody searches for that. It leads with what people already type into a search bar: *product QR generator, warranty QR code, digital product page, QR for packaging.* GS1 compliance, DPP-readiness, and event-grade identity all happen invisibly behind that simple entry point.

With no paid acquisition budget, the realistic channels are:

- **SEO on real search terms** — nobody has written the plain-English explainer for GS1 Sunrise; that content ranks by default today.
- **Embedded distribution** — packaging designers, label printers, and co-packers already touch every product going through this transition; a white-label or partner integration reaches thousands of SKUs through a handful of relationships.
- **The free tier itself as the acquisition engine** — because it produces a visible, forwardable artifact (Section 12), free users become the internal sales motion, not just leads.

---

# 12. Closing the Buyer Gap

The person who sets up free routing is rarely the person who signs off on a six-figure supplier recovery contract. Left alone, that gap stalls the funnel indefinitely.

The fix is mechanical, not aspirational: the dashboard itself generates the pitch. *"450 scans this month came from unregistered service centers. Here's what that could be costing you in warranty exposure — forward this to your VP of Quality."* The free user becomes the one who hands the enterprise case to the budget owner, because the product did the work of finding the number, not because anyone was asked to advocate internally.

---

# 13. The Definition

> **Zyppi is the identity and routing layer for physical products.**
>
> Every product receives a permanent digital identity. Whenever that identity is accessed, Zyppi determines the context, logs the event, and routes the person or system to the correct destination — without hosting the underlying content and without replacing the systems a company already runs.

Not a QR company. Not a DPP platform. Not a CMS. The infrastructure that decides, in milliseconds, where every physical-world interaction should go — and remembers that it happened.

---

# 14. The Long Arc

Today, this starts as a five-minute setup: upload a product list, get permanent identities, define a few routing rules. The value compounds without anyone doing anything differently — because the interactions were already happening.

Over time, the same infrastructure that routes a consumer to a manual routes a regulator to a compliance record, a technician to a service history, an AI agent to a verified authenticity check, and a supplier chargeback to the exact event that triggered it. None of these are new products. They are what becomes possible once every physical product has one identity, one address, and a permanent, verifiable record of everything that happened to it.

**Identify once. Route forever.**
