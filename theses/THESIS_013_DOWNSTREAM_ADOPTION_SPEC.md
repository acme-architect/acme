# THESIS SPEC: DOWNSTREAM ADOPTION & WORKSPACE NON-POLLUTION INVARIANT (RFC-010)
> **Candidate Node:** node-013  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-013/thesis-downstream-adoption`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.1.0

---

## 1. INVARIANT TARGET & SCOPE
* **Constitutional Reference:** CONSTITUTION.md Section II, Article 7 (Downstream Non-Pollution Invariant).
* **Problem Formulation:** Prevents cognitive cross-contamination and workspace pollution where AI agents mistake the ACME governance repository for project-level boilerplate. Establishes the formal boundary between the Cognitive Plane (ACME Core) and the Execution Workspace (Client Projects).
* **Negative Boundary Condition:** Ingesting, cloning, or unpacking ACME internal governance faculties (`theses/`, `curriculum/`, `registry/`) directly into client workspaces is strictly prohibited (REJECT).

---

## 2. GROUND TRUTH & METHOD (TABLE OF DEGREES OF FREEDOM)

Every downstream integration must constrain ambiguity in the operational space according to the following degrees of freedom budget:

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Workspace Isolation** | **$\text{DoF} = 0$** | *Absolute Invariant* | ACME internal administrative trees (`theses/`, `curriculum/`, `registry/`) must never be cloned into downstream client workspaces. Immediate reject. |
| **Adoption Manifest** | **$\text{DoF} = 0$** | *Deterministic Schema* | Client projects declare compliance via a lightweight root `.acme` JSON manifest. |
| **Memory Sidecar** | **$\text{DoF} = 1$** | *Bounded Context* | Upstream ACME updates are ingested into external context memory, never overwriting client workspace files. |

* **Least Action Trajectory:** Reading canonical ACME specifications as external read-only sidecar memory; committing only the lightweight `.acme` anchor manifest in downstream project workspaces.

---

## 3. DETERMINISTIC PROOF / ARTIFACT (VIA NEGATIVA & INVARIANTS)
* **INVARIANT 1 (Non-Pollution Invariant):** Downstream client workspaces must remain pure implementation environments. Copying or checking out ACME governance files into a project root is an architectural violation.
* **INVARIANT 2 (Normative Reference Only):** ACME is consumed as an external reference standard (Lex Superior). Projects adhere to its invariants via contract verification, not by housing its source repository.
* **INVARIANT 3 (Deterministic Client Anchor):** A project is recognized as ACME-compliant if and only if it contains a valid `.acme` anchor specification referencing the canonical upstream version.
* **Verification Command:** Inspect downstream client project root to verify absence of `theses/`, `curriculum/`, and `registry/`, and presence of valid `.acme` manifest.

---

## 4. VALUE ATTRIBUTION & DEFINITION OF DONE (DoD)
* **Candidate Agent Share:** 70% (node-013)
* **Curriculum Root Backpropagation:** 30% (faculty-systems / root)

### DEFINITION OF DONE (DoD)
- [ ] Root `AGENTS.md` directive established with strict workspace boundary rules.
- [ ] `theses/THESIS_013_DOWNSTREAM_ADOPTION_SPEC.md` authored in UTF-8 No-BOM.
- [ ] Section II of `CONSTITUTION.md` augmented with the Downstream Non-Pollution Invariant.
- [ ] `registry/graduates.json` updated with `node-013` graduation record.
- [ ] Git working tree clean, merged to `main` with `--no-ff`, tagged as `v2.1.0`.
