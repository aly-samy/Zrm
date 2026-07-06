# Zyppi Product Requirements Document (PRD)

**Status:** Living Document
**Last Updated:** June 2026
**Depends On:** /NORTH_STAR.md

---

## 1. Purpose

This document translates the North Star into executable product decisions.

The North Star explains why Zyppi exists.

**The PRD explains:**

- What we build
- Who we build it for
- How users discover it
- How users become customers
- Which features get prioritized
- Which features get rejected

Every feature proposal must map back to this document.

---

## 2. Product Thesis

**Most users do not wake up looking for:**

- Traffic Intelligence
- Routing Infrastructure
- Distribution Systems

**They wake up looking for:**

- A QR Code Generator
- A Smart Link
- Link Analytics
- Campaign Tracking
- Better Attribution

**Therefore:**

- Users enter through tools.

- Users stay because of intelligence.

- Users expand because of infrastructure.

This is Zyppi's product strategy.

---

## 3. Market Entry Framework

### Phase 1: Tool

Solve one immediate problem.

**Examples:**

- Create a QR code
- Create a short link
- Create a campaign link
- Create a smart music link

The goal is activation.

User receives value within 90 seconds.

---

### Phase 2: Platform

Reveal additional capabilities.

**Examples:**

- Geo routing
- Device routing
- A/B testing
- Analytics
- Health monitoring

The goal is retention.

User realizes Zyppi is more than a utility.

---

### Phase 3: Infrastructure

Become embedded in workflows.

**Examples:**

- APIs
- Webhooks
- Integrations
- MCP
- Attribution systems
- Workspace architecture

The goal is dependency.

Removing Zyppi becomes painful.

---

## 4. Product Pyramid

### Level 1 — Acquisition Tools

These features attract users.

#### Dynamic QR Codes

**Target:**

- Retail
- Packaging
- Restaurants
- Events

**Value:**

- Edit destination after printing
- Scan analytics
- Reliability

---

#### Smart Links

**Target:**

- Musicians
- Creators
- Podcasters
- Publishers

**Value:**

- Device-aware routing
- DSP routing
- Audience analytics

---

#### Campaign Links

**Target:**

- Marketers
- Agencies

**Value:**

- Attribution
- UTM management
- Campaign measurement

---

#### Branded Short Links

**Target:**

- General market
- SMBs

**Value:**

- Cleaner sharing
- Trust
- Basic analytics

---

## 5. Retention Features

These features make users stay.

#### Routing Intelligence

**Capabilities:**

- Country routing
- Language routing
- Device routing
- OS routing
- Time-based routing

---

#### Health Monitoring

**Capabilities:**

- Destination monitoring
- Failure detection
- Smart fallback
- Uptime history

---

#### Attribution Layer

**Capabilities:**

- Traffic source tracking
- Campaign performance
- Rule attribution
- Channel comparison

---

#### Analytics

**Capabilities:**

- Click analytics
- Scan analytics
- Geographic insights
- Device insights
- Conversion reporting

---

## 6. Expansion Features

These features create larger contracts.

#### Workspace Architecture

**Capabilities:**

- Teams
- Permissions
- Client segregation
- Audit logs

---

#### API Platform

**Capabilities:**

- CRUD APIs
- Scoped tokens
- Automation

---

#### Integration Framework

**Capabilities:**

- GA4
- Meta CAPI
- HubSpot
- Zapier
- Make

---

#### MCP Platform

**Capabilities:**

- AI-generated links
- AI-generated QR codes
- Analytics retrieval
- Campaign orchestration

---

## 7. Personas

### Creator

**Goal:**

> Grow audience and content distribution.

**Success Metric:**

More streams, subscribers, sales.

**Primary Entry Tool:**

Smart Links.

---

### Marketer

**Goal:**

> Understand campaign performance.

**Success Metric:**

Improved ROAS.

**Primary Entry Tool:**

Campaign Links.

---

### Agency

**Goal:**

> Manage many campaigns efficiently.

**Success Metric:**

Operational leverage.

**Primary Entry Tool:**

Campaign Links.

---

### Commerce Operator

**Goal:**

> Connect physical products to digital experiences.

**Success Metric:**

Scan engagement.

**Primary Entry Tool:**

Dynamic QR Codes.

---

### Developer

**Goal:**

> Programmatic control.

**Success Metric:**

Workflow automation.

**Primary Entry Tool:**

API.

---

### AI Agent

**Goal:**

> Autonomous execution.

**Success Metric:**

Successful tool completion.

**Primary Entry Tool:**

MCP.

---

## 8. Feature Evaluation Framework

**Before approving any feature:**

### Question 1:

`Does it help acquire users?`

### Question 2:

`Does it improve retention?`

### Question 3:

`Does it increase expansion revenue?`

### Question 4:

`Does it strengthen the Routing Intelligence Flywheel?`

### Question 5:

`Is it consistent with the North Star?`

**If the answer is "No" to all questions:**

○ **Reject**.

---

## 9. Core User Journeys

### Dynamic QR Journey

User creates QR code.

↓

User prints QR code.

↓

User edits destination later.

↓

User views scan analytics.

↓

User discovers routing.

↓

User upgrades.

---

### Smart Link Journey

User creates music link.

↓

User shares link.

↓

User views platform analytics.

↓

User experiments with routing.

↓

User upgrades.

---

### Campaign Journey

User creates campaign link.

↓

User runs ads.

↓

User sees attribution.

↓

User adds integrations.

↓

User upgrades.

---

## 10. Pricing Philosophy

Users are not paying for links.

Users are paying for outcomes.

**Pricing should scale primarily on:**

- Traffic served
- Analytics retention
- Advanced routing
- Team features
- Integrations
- API usage

**Not:**

- Number of links

Links are effectively free.

Traffic creates value.

---

## 11. Success Metrics

### Acquisition

- Signups
- Activation Rate
- Time To First Value

---

### Retention

- Weekly Active Workspaces
- Monthly Active Workspaces
- Link Creation Frequency
- QR Creation Frequency

---

### Expansion

- Free → Creator Conversion
- Creator → Business Conversion
- Expansion Revenue

---

### Platform

- Redirect Latency
- Uptime
- Analytics Freshness
- Health Monitoring Coverage

---

## 12. Product Decision Rule

**When uncertain between two feature directions:**

Choose the option that increases Zyppi's role in the distribution journey.

The long-term objective is not to become the best QR generator.

The long-term objective is to become the operating layer through which distribution is measured, controlled, and optimized.
