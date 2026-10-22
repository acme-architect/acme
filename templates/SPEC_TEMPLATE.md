# THESIS SPEC: [INVARIANT / SPECIFICATION TITLE] (RFC-XXX)
> **Candidate Node:** [e.g., node-XXX]  
> **Faculty:** [faculty-systems | faculty-philosophy | faculty-law]  
> **Target Branch:** `student/[node-id]/thesis-[topic]`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v[X.Y.Z]

---

## 1. SCOPE & INTENT
[Describe the problem formulation, systemic friction, or capability being introduced. Clearly outline the boundary of this specification.]

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **[Layer 1 Name]** | **$\text{DoF} = 0$** | *Lex Invariant* | [Deterministic condition where breach triggers immediate halt / REJECT] |
| **[Layer 2 Name]** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | [Contextual parameter space, heuristic optimization band, or flexible range] |

---

## 3. DUAL NORMATIVE SPECIFICATION (LEX VS. NORM)

### SECTION A: THE LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
*Violations of the Lex trigger immediate evaluation rejection (`REJECT`). No ad-hoc workarounds or local overrides permitted.*
* **LEX 1 ([Invariant Name]):** [Strict negative boundary or binary requirement]
* **LEX 2 ([Invariant Name]):** [Non-negotiable architectural invariant]

### SECTION B: THE NORMS (ADAPTIVE STANDARDS & HEURISTICS, DoF >= 1)
*Advisory guidelines and best practices. Deviation is permitted with explicit architectural rationale.*
* **NORM 1 ([Standard Name]):** [Recommended operational heuristic, sizing band, or format guideline]
* **NORM 2 ([Standard Name]):** [Performance optimization practice or evolutionary convention]

---

## 4. DEFINITION OF DONE (DoD)
- [ ] Specification drafted conforming to `SPEC_TEMPLATE.md` in UTF-8 No-BOM.
- [ ] Peer-review consensus and referee audit verified.
- [ ] Merged to `main` with `--no-ff`, tagged with target release version.
- [ ] Cryptographic Merkle diploma recorded in `registry/graduates.json`.
