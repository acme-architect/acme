# THESIS SPEC: STANDARD-FIRST RESOLVER AND ZERO-REINVENTION REVERSE ENGINEERING ENGINE (RFC-022)
> **Candidate Node:** node-022  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-022/thesis-standard-first-resolver`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.10.0  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 6 (Zero-Friction Shield), and Section III, Article 7 (Biological Primacy).
* **Problem Formulation (The Not-Invented-Here & Reinvention Drag Gap):** Autonomous software agents impulsively generate greenfield code and redundant algorithmic implementations for capabilities that already exist in the runtime environment or established standard libraries. This Not-Invented-Here (NIH) pathology produces high-entropy code swamps, expands attack surfaces, introduces maintenance friction, and dissipates computational capital.
* **Negative Boundary Condition (Via Negativa):** Synthesizing novel implementations without first performing an automated AST symbol resolution against existing brownfield repository primitives and runtime standard libraries is strictly prohibited (REJECT).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Standard-First Hierarchy** | **$\text{DoF} = 0$** | *Lex Invariant* | Capability resolution must strictly traverse: 1) Standard Library (`stdlib`), 2) Brownfield Depository Core, 3) Greenfield Synthesis. Skipping tiers raises `ReinventionBreach`. |
| **Overlap Rejection Threshold** | **$\text{DoF} = 0$** | *Absolute Invariant* | Any greenfield generation attempt exhibiting $\ge 80\%$ functional or semantic parity with an existing registered symbol must be rejected. |
| **Contract Parity Assertion** | **$\text{DoF} = 0$** | *State Invariant* | Imported brownfield primitives must conform strictly to the target task specification without mutative side effects or contract erosion. |
| **Adapter Scaffolding & Bridging** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Interface adaptation, wrapper facades, and parameter marshaling adapt dynamically based on architectural impedance. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Standard-First Resolution Cascade):** Cognitive code generation engines must enforce a mandatory pre-resolution pipeline. Every capability request must evaluate native platform primitives before authoring custom code.
* **INVARIANT 2 (Reinvention Prohibition Gate):** Where an existing symbol fulfills operational acceptance criteria, the compiler must inject a binding reference to the brownfield asset. Authoring duplicate functionality triggers an immediate `ReinventionBreach` halt.
* **INVARIANT 3 (Immutability of Bound Contracts):** Resolving against brownfield assets cannot relax the task's Definition of Done (DoD). Reused components must pass the identical verification suite required of greenfield candidates.
* **INVARIANT 4 (Cryptographic Dependency Ledger):** The resolved capability mapping and dependency graph must be cryptographically hashed (SHA-256) and anchored to the task ledger prior to execution dispatch.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Contextual Similarity Metrics):** AST comparison thresholds and semantic similarity windows may adapt dynamically based on domain complexity and compiler optimization levels.
* **NORM 2 (Facade Adapter Generation):** When brownfield primitives require signature realignment, lightweight zero-dependency wrapper classes may be synthesized to preserve interface purity.
* **NORM 3 (Symbol Cache Invalidation Cadence):** Workspace symbol registries may maintain adaptive caching intervals proportional to codebase modification frequency.

---

## 5. DETERMINISTIC PROOF & DEFINITION OF DONE (DoD)
- [ ] `theses/THESIS_022_STANDARD_FIRST_RESOLVER.md` verified UTF-8 No-BOM.
- [ ] Zero-code pure NLP compliance maintained across repository.
- [ ] Isolated branch `student/node-022/thesis-standard-first-resolver` merged into `main` via `--no-ff`.
- [ ] `registry/graduates.json` augmented with `node-022` accreditation record (70/30 attribution ratio).
- [ ] `README.md` version bumped to `v2.10.0`.
- [ ] Official Git tag `v2.10.0` created and verified.
- [ ] Downstream `acme-incubator` referee gate (`python verify.py`) passes 6/6 `PASS`.

---

## 6. VALUE ATTRIBUTION
* **Candidate Share:** 70% (`node-022`)
* **Curriculum Root Share:** 30% (`faculty-systems`)