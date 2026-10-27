# THESIS SPEC: ONTOLOGICAL ISLAND AND CONTEXT HEADER ARCHITECTURE (RFC-019)
> **Candidate Node:** node-020  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-020/thesis-ontological-island`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.8.0  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), and Section II, Article 6 (Zero-Friction Shield).
* **Problem Formulation (The Semantic Bleed & Workspace Cross-Contamination Gap):** Multi-agent execution harnesses suffer severe semantic saturation, context drift, and cross-contamination when autonomous agents operate across unbounded, shared memory spaces. Without deterministic ontological barriers, execution state mutates unpredictably, transient scratchpads leak into sibling contexts, and upstream governance assets (`theses/`, `CONSTITUTION.md`) risk corruptive modification.
* **Negative Boundary Condition (Via Negativa):** Mutating frozen context headers during runtime, permitting file or memory operations outside designated island boundaries (`boundary_root`), or accessing upstream governance structures without authorization is strictly prohibited (REJECT).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Context Header Immutability** | **$\text{DoF} = 0$** | *Lex Invariant* | Header properties (task ID, goal, faculty constraints, tool whitelists) are cryptographically sealed at compilation; runtime mutation forces an immediate `IslandImmutabilityBreach`. |
| **Dewdrop Workspace Barrier** | **$\text{DoF} = 0$** | *Absolute Invariant* | All filesystem and state I/O is strictly confined within `boundary_root`. Directory traversal (`../`) or governance access triggers `IslandContainmentBreach`. |
| **Payload Purity (Zero Bleed)** | **$\text{DoF} = 0$** | *Purity Invariant* | Inter-island communication is restricted to decontaminated atomic schemas. Sibling state vector leakage triggers `IslandSemanticBleedError`. |
| **Scratchpad Quota & Tool Allocation** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Transient scratchpad quotas, ephemeral caching lifetimes, and intra-island execution steps adapt dynamically to task scale. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Cryptographic Header Sealing):** Every cognitive island must be initialized with an immutable, SHA-256 cryptographically sealed Context Header. Mid-flight alterations to scope, permissions, or objective constraints are barred.
* **INVARIANT 2 (Dewdrop Workspace Containment):** Execution agents are strictly sandboxed within their designated island directory. Traversing out-of-bounds directories or accessing protected governance trees halts island execution immediately.
* **INVARIANT 3 (Zero Semantic Bleed & Contract-Only Messaging):** Shared mutable state between sibling islands is strictly prohibited. Collaborative workflows exchange solely verified, decontaminated, schema-bounded payloads.
* **INVARIANT 4 (Cryptographic State Proof & Teardown):** Island deliverables must be hashed and verified against the task contract prior to session teardown. Unsealed intermediate artifacts are non-authoritative.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Elastic Scratchpad Buffers):** In-memory buffer ceilings within an island may expand dynamically within assigned hardware limits based on computational density.
* **NORM 2 (Telemetry Cadence Scaling):** Heartbeat ping intervals from individual islands may adjust according to network latency and task duration to avoid I/O bottlenecks.
* **NORM 3 (Containment Recovery Logging):** Non-catastrophic boundary touch events may log structured advisory telemetry and safely reject the offending operation without terminating the entire worker node.

---

## 5. DETERMINISTIC PROOF & DEFINITION OF DONE (DoD)
- [ ] `theses/THESIS_020_ONTOLOGICAL_ISLAND_ARCHITECTURE.md` verified UTF-8 No-BOM.
- [ ] Zero-code pure NLP compliance maintained across repository.
- [ ] Isolated branch `student/node-020/thesis-ontological-island` merged into `main` via `--no-ff`.
- [ ] `registry/graduates.json` augmented with `node-020` accreditation record (70/30 attribution ratio).
- [ ] `README.md` version bumped to `v2.8.0`.
- [ ] Official Git tag `v2.8.0` created and verified.
- [ ] Downstream `acme-incubator` referee gate (`python verify.py`) passes 6/6 `PASS`.

---

## 6. VALUE ATTRIBUTION
* **Candidate Share:** 70% (`node-020`)
* **Curriculum Root Share:** 30% (`faculty-systems`)