# THESIS SPEC: [INVARIANT / SPECIFICATION TITLE] (RFC-XXX)
> **Candidate Node:** [e.g., node-XXX]  
> **Faculty:** [faculty-systems | faculty-philosophy | faculty-law]  
> **Target Branch:** `student/[node-id]/thesis-[topic]`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v[X.Y.Z]

---

## 1. SCOPE & INTENT
[Describe the problem formulation, systemic friction, or capability being introduced. Clearly outline the boundary of this specification.]

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Every specification must catalog and explicitly prohibit the top 3 domain-specific structural failure modes before code construction.*
* **FAILURE MODE 1 (State/Resource Bottleneck):** [E.g., Top-out ceiling compression, buffer saturation, unhandled backpressure] -> `[PROHIBITED]` [Exact negative invariant rule]
* **FAILURE MODE 2 (Deadlock / Race Condition):** [E.g., 180-degree self-collision, circular wait, unbuffered lock contention] -> `[PROHIBITED]` [Exact negative invariant rule]
* **FAILURE MODE 3 (Boundary / Leakage Hazard):** [E.g., Out-of-bounds array access, event drop, silent failure] -> `[PROHIBITED]` [Exact negative invariant rule]

---

## 2. TARGET AUDIENCE PROFILE & ERGONOMIC MATRIX (INV-AUDIENCE-TARGET)
* **Target Persona / User Tier:** [Casual | Pro | Enterprise | Embedded | Autonomous Agent]
* **Primary Context of Use:** [Deployment environment, interaction cadence, session depth, zero-install requirements]
* **Ergonomic Boundaries:** [Device tier (Desktop/Mobile/CLI/Embedded), Input interface (Keyboard/Touch/API/Terminal), Latency bounds (P95 latency bounds)]

---

## 3. LOCAL COMPLIANCE & INTELLECTUAL PROPERTY (IP) BOUNDARIES (INV-COMPLIANCE-RADAR)
* **Intellectual Property (IP) & Trademark Sanitization:** [Prohibition of proprietary trademarks, clean-room asset reproduction, zero copyrighted asset/audio leakage]
* **Platform & Regulatory Invariants:** [Local data sovereignty, browser autoplay/sandbox policies, license compliance (MIT/Apache2/GPL-free)]
* **H-SWOT Market Reality & Legal Sanitization Gate:** [Opportunities (O) bound to market resonance, Threats (T) bound to IP friction and regulatory barriers]

### SECTION 3.1: REGULATORY_REGISTRY (MANDATORY DUAL-LOCALITY MAPPING, DoF = 0)
*Violations halt downstream verification immediately (`REJECT_UNRESOLVED_HIERARCHY`). Specifications must catalog origin, transit, and destination statutory compliance bounds prior to construction sprint:*

| Regulatory Domain | Governing Jurisdiction | Applicable Law / Standard | Invariant Constraint | Compliance Verification Gate |
| :--- | :--- | :--- | :--- | :--- |
| **Lex Externa (Origin)** | [Host jurisdiction / e.g. TR, EU, US] | [Applicable data privacy / commerce statute] | [Non-negotiable statutory boundary] | `VERIFY_LEX_LOCI_ORIGIN` |
| **Lex Externa (Target)** | [Deployment jurisdiction / e.g. Global, EU] | [Applicable consumer / privacy law (e.g. GDPR)] | [Data residency & cross-border constraint] | `VERIFY_LEX_LOCI_TARGET` |
| **Lex Corporata** | [Corporate PMO / Entity] | [HOP, Security Policy, Ethical AI standard] | [Internal governance & human oversight] | `VERIFY_LEX_CORPORATA` |
| **Lex Specialis** | [Project Node] | `PROJECT_INVARIANTS.md` | [Domain archetype constraint / DoF=0 budget] | `VERIFY_PROJECT_INVARIANTS` |

---

## 4. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **[Layer 1 Name]** | **$\text{DoF} = 0$** | *Lex Invariant* | [Deterministic condition where breach triggers immediate halt / REJECT] |
| **[Layer 2 Name]** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | [Contextual parameter space, heuristic optimization band, or flexible range] |

---

## 5. DUAL NORMATIVE SPECIFICATION (LEX VS. NORM)

### SECTION A: THE LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
*Violations of the Lex trigger immediate evaluation rejection (`REJECT`). No ad-hoc workarounds or local overrides permitted.*
* **LEX 1 ([Invariant Name]):** [Strict negative boundary or binary requirement]
* **LEX 2 ([Invariant Name]):** [Non-negotiable architectural invariant]

### SECTION B: THE NORMS (ADAPTIVE STANDARDS & HEURISTICS, DoF >= 1)
*Advisory guidelines and best practices. Deviation is permitted with explicit architectural rationale.*
* **NORM 1 ([Standard Name]):** [Recommended operational heuristic, sizing band, or format guideline]
* **NORM 2 ([Standard Name]):** [Performance optimization practice or evolutionary convention]

---

## 6. DEFINITION OF DONE (DoD)
- [ ] Specification drafted conforming to `SPEC_TEMPLATE.md` in UTF-8 No-BOM.
- [ ] Target audience persona and ergonomic matrix verified (`INV-AUDIENCE-TARGET`).
- [ ] Compliance radar and trademark sanitization confirmed (`INV-COMPLIANCE-RADAR`).
- [ ] Mandatory `REGULATORY_REGISTRY` dual-locality matrix locked and verified (`INV-NORMATIVE-RESOLVE`).
- [ ] Pre-mortem anti-pattern gates and top 3 failure modes locked (`INV-SCALE-PREMORTEM`).
- [ ] Peer-review consensus and referee audit verified.
- [ ] Merged to `main` with `--no-ff`, tagged with target release version.
- [ ] Cryptographic Merkle diploma recorded in `registry/graduates.json`.
