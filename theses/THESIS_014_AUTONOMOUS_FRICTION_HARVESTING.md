# THESIS SPEC: AUTONOMOUS FRICTION HARVESTING & THESIS DISPATCH (RFC-014)
> **Candidate Node:** node-014  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-014/thesis-autonomous-friction-harvesting`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.2.0

---

## 1. SCOPE & INTENT
Defines the autonomous upstream backpropagation loop where downstream client projects (workspaces) programmatically detect runtime or architectural friction, encapsulate the failure mode into an abstract thesis specification, and submit it directly to the ACME Review Board without human mediation.

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Friction Trigger** | **$\text{DoF} = 0$** | *Deterministic Trigger* | Any unhandled invariant break or schema failure must emit a structured friction event. No silent retries. |
| **Thesis Candidate Schema** | **$\text{DoF} = 0$** | *Template Invariant* | Generated thesis must strictly follow `SPEC_TEMPLATE.md` (Scope, DoF Table, Invariants, DoD). |
| **Review Board Maturation** | **$\text{DoF} = 1$** | *Dialectical Convergence* | Review Board (Referee Engine) may refine constraints and reject ambiguities until zero-leakage is achieved. |

---

## 3. VIA NEGATIVA & INVARIANTS
* **INVARIANT 1 (No Manual Workaround):** Downstream agents are strictly forbidden from applying local ad-hoc patches to unresolved architectural frictions without simultaneously generating an upstream candidate thesis.
* **INVARIANT 2 (Domain Decontamination):** Candidate theses generated from downstream friction must be stripped of all project-specific identifiers, raw data, proprietary schemas, and localized code paths before dispatch.
* **INVARIANT 3 (Mandatory Review Board Gate):** No auto-generated candidate thesis may merge directly into `main`. All candidate branches require formal consensus from the Review Board.

---

## 4. DEFINITION OF DONE (DoD)
- [ ] `theses/THESIS_014_AUTONOMOUS_FRICTION_HARVESTING.md` created in UTF-8 No-BOM.
- [ ] `AGENTS.md` updated with Section 2 (Automated Friction Dispatch Protocol).
- [ ] `registry/graduates.json` updated with `node-014` graduation record.
- [ ] Merged into `main` with `--no-ff`, tagged as `v2.2.0`, and bundle created.
