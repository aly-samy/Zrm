# Zyppi Technical Architecture Bible

**Status:** Living Document
Last Updated: June 2026
Depends On:
- /NORTH_STAR.md
- /PRD.md

## Purpose:

Define the engineering principles, system boundaries, architectural decisions, and operational constraints that govern the Zyppi platform.

**This document explains how Zyppi is built and why it is built that way.**

---

## 1. Architecture Philosophy

Zyppi is not a website.

Zyppi is not a dashboard.

Zyppi is not a CRUD application.

Zyppi is a traffic infrastructure platform.

**The architecture must therefore optimize for:
**
1. Routing Speed
2. Reliability
3. Scalability
4. Observability
5. Simplicity

Every technical decision should improve one or more of these dimensions.

---

## 2. Core Architectural Principles

### Principle 1: Redirects Are Sacred

The redirect path is the most important path in the system.

A dashboard can be slow.

A report can be delayed.

A redirect cannot fail.

Every architectural decision must protect redirect performance first.

---

### Principle 2: Read Fast, Write Eventually

Traffic volume is significantly larger than configuration volume.

**Therefore:**

- Reads must be optimized.
- Writes can be asynchronous.

**The platform should always prefer:**

Fast reads.

Cheap writes.

Distributed caching.

Asynchronous processing.

---

### Principle 3: Intelligence Must Never Block Traffic

Analytics are valuable.

Routing is essential.

**If analytics fail:**

Traffic continues.

**If queues fail:**

Traffic continues.

**If reporting fails:**

Traffic continues.

Nothing outside routing may block a redirect.

---

### Principle 4: Every Component Has One Job

Workers should have clearly defined responsibilities.

Avoid large multi-purpose services.

Small focused services scale better.

Debug easier.

Deploy safer.

---

### Principle 5: Event-Driven Over Synchronous

**Whenever possible:**

Emit events.

Consume asynchronously.

Avoid tightly coupled service dependencies.

---

## 3. System Overview

Zyppi consists of three layers.

---

### Layer 1: Traffic Layer

**Responsible for:**

- Redirect execution
- Rule evaluation
- Bot detection
- Health verification

**Requirements:**

- Ultra-low latency
- High availability
- Global execution

This layer generates revenue.

This layer receives the most protection.

---

### Layer 2: Intelligence Layer

**Responsible for:**

- Analytics
- Attribution
- Reporting
- Aggregation

**Requirements:**

- Event-driven
- Horizontally scalable
- Query efficient

This layer creates retention.

---

### Layer 3: Management Layer

**Responsible for:**

- Dashboard
- Billing
- Users
- Workspaces
- Configuration

**Requirements:**

- Reliability
- Maintainability

This layer creates usability.

---

## 4. System Boundaries

The platform is divided into bounded domains.

---

### Routing Domain

**Owns:**

- Links
- Rules
- Destinations
- Traffic decisions

**Does NOT own:**

- Billing
- Users
- Analytics

---

### Analytics Domain

**Owns:**

- Click events
- Scan events
- Aggregations
- Reports

**Does NOT own:**

- Routing decisions

---

### Identity Domain

**Owns:**

- Authentication
- Authorization
- Sessions

**Does NOT own:**

- Business logic

---

### Billing Domain

**Owns:**

- Plans
- Entitlements
- Usage
- Subscriptions

**Does NOT own:**

- Authentication
- Routing

---

### Integration Domain

**Owns:**

- Webhooks
- APIs
- MCP
- External systems

**Does NOT own:**

- Core routing

---

## 5. Traffic Architecture

The redirect engine is Zyppi's core asset.

**Requirements:**

- Global availability
- Stateless execution
- Deterministic routing

**A redirect request should require:**

1. Route lookup
2. Rule evaluation
3. Destination selection
4. Redirect response

Nothing more.

Every additional step increases risk.

---

## 6. Routing Engine Rules

**The routing engine must remain:**

- Pure
- Deterministic
- Testable

**The routing engine may never:**

- Make network requests
- Read external services
- Call APIs
- Write to databases

**Input:**

Context

**Output:**

Destination

This guarantees predictable behavior.

---

## 7. Analytics Architecture

Analytics is a consumer of traffic.

Never a dependency of traffic.

**Flow:**

Redirect

↓

Event Generated

↓

Queue

↓

Storage

↓

Aggregation

↓

Reporting

Failure at any stage must not affect routing.

---

## 8. Event Architecture

Events are first-class citizens.

Every significant action should emit events.

**Examples:**

- Link Created
- Link Updated
- Link Deleted
- Link Clicked
- QR Scanned
- Workspace Created
- Plan Changed
- Health Alert Triggered

**Benefits:**

- Decoupling
- Auditability
- Future integrations
- AI workflows

---

## 9. Caching Strategy

Caching exists to protect latency.

**Rules:**

Cache aggressively.

Invalidate precisely.

Never rely on cache as source of truth.

Source of truth always remains persistent storage.

Cache is acceleration.

Not authority.

---

## 10. Security Principles

### Least Privilege

Every token receives minimum required permissions.

---

### Zero Trust

Every request is authenticated.

Every request is authorized.

Internal traffic is not trusted automatically.

---

### Auditability

Every write operation must be traceable.

Who.

When.

What changed.

---

### Secret Isolation

**Secrets never appear:**

- In logs
- In analytics
- In client applications

---

## 11. Reliability Standards

### Redirect Reliability

**Target:**

99.99%

---

### Dashboard Reliability

**Target:**

99.9%

---

### API Reliability

**Target:**

99.9%

---

### Analytics Freshness

**Target:**

Under 60 seconds

---

### Health Monitoring

**Target:**

90%+ active coverage

---

## 12. AI Architecture

AI is not an add-on.

AI is a first-class interface.

**Users interact through:**

1. Dashboard
2. API
3. AI Agent

All three should expose equivalent capabilities.

**An AI agent should be able to:**

- Create links
- Create QR codes
- Read analytics
- Manage campaigns

without requiring a human dashboard session.

---

## 13. Integration Strategy

Every integration must satisfy at least one goal:

### Distribution

**Example:**

- WordPress
- Shopify
- CMS platforms

---

### Attribution

**Example:**

- GA4
- Meta
- HubSpot

---

### Automation

**Example:**

- Zapier
- Make
- n8n

---

> Integrations that do not improve distribution, attribution, or automation should be rejected.

---

## 14. Architecture Decision Records (ADR)

Every major architectural decision requires an ADR.

### ADR structure:

- Context
- Decision
- Alternatives Considered
- Consequences

**Examples:**

ADR-001 Edge Infrastructure

ADR-002 Analytics Platform

ADR-003 Authentication Provider

ADR-004 Billing Architecture

ADR-005 MCP Architecture

This creates institutional memory.

---

## 15. Technical Decision Framework

Before introducing a new technology ask:

1. Does it improve routing performance?
2. Does it improve reliability?
3. Does it reduce operational complexity?
4. Does it strengthen observability?
5. Can the same outcome be achieved using existing infrastructure?

If not, do not introduce it.

---

## 16. Long-Term Technical Vision

Most companies build applications.

Zyppi is building infrastructure.

The long-term objective is to become the operating layer through which digital distribution flows.

Every technical decision should move the platform toward:

- Greater control.

- Greater intelligence.

- Greater automation.

Without compromising the speed and reliability of the traffic layer.
