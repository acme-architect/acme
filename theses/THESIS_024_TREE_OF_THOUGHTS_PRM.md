# THESIS SPEC: TREE OF THOUGHTS AND PROCESS REWARD MODEL SEARCH HARNESS (RFC-023)
> **Candidate Node:** node-024  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-024/thesis-tree-of-thoughts`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.12.0  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 6 (Zero-Friction Shield), and Section III, Article 7 (Biological Primacy).
* **Problem Formulation (The Outcome-Only Evaluation & Combinatorial Runaway Gap):** Autonomous multi-step reasoning agents evaluated exclusively at terminal task completion (Outcome Reward Models - ORM) suffer exponential compounding of intermediate errors. A single flawed intermediate premise contaminates all subsequent generation, consuming vast token budgets on irrecoverable execution branches.
* **Negative Boundary Condition (Via Negativa):** Proceeding along reasoning trajectories without validating intermediate steps, attempting to generate descendant branches from sub-threshold nodes ($S_{\text{step}} < 0.70$), failing to backtrack deterministically upon path exhaustion, or exceeding search horizon bounds is strictly prohibited (REJECT).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Step-Level PRM Scoring** | **$\text{DoF} = 0$** | *Lex Invariant* | Each intermediate reasoning step must be evaluated independently. Scores below threshold ($S < 0.70$) force immediate branch pruning (`PRUNE_BRANCH`). |
| **Deterministic Backtracking** | **$\text{DoF} = 0$** | *State Invariant* | When an active trajectory exhausts viable child nodes, the execution engine must unwind cleanly to the nearest validated ancestor state. |
| **Search Horizon Ceiling** | **$\text{DoF} = 0$** | *Absolute Invariant* | Tree depth ($\text{depth} \le D_{\max}$) and beam width ($\text{beam} \le B_{\max}$) are strictly bounded. Breaching caps raises `CombinatorialExplosionBreach`. |
| **Heuristic Weighting & Beam Allocation** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Evaluation metric weights, candidate branch expansion factors, and domain-specific heuristics adapt dynamically to problem complexity. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Step-Level PRM Validation Gate):** Multi-step cognitive tasks must evaluate step validity at each transition boundary. Descendant state exploration from unverified or sub-threshold intermediate steps is forbidden.
* **INVARIANT 2 (Deterministic Ancestor Backtracking):** When all child states of a node fail validation, the search engine must trip a localized circuit breaker and regress to the nearest ancestor with unexpanded viable frontiers. Infinite retry loops on dead paths are barred.
* **INVARIANT 3 (Bounded Search Horizon Invariant):** The state tree must operate within explicit combinatorial ceilings. Unbounded recursion or speculative fan-out terminates execution with a bounded early-exit exception.
* **INVARIANT 4 (Cryptographic Trajectory Ledger):** The chosen optimal path, parent-child transitions, and step evaluation scores must be hashed (SHA-256) and recorded in the audit ledger upon goal achievement.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Context-Aware Scoring Profiles):** PRM scoring weights and acceptance thresholds may tighten in safety-critical domains and relax during speculative hypothesis generation.
* **NORM 2 (Adaptive Beam Pruning):** Search beam widths may dynamically contract as confidence margins widen across competing candidate steps.
* **NORM 3 (Pruned Node Telemetry Compaction):** Diagnostic metrics for rejected search branches may be stored in compressed summary digests to conserve memory bandwidth.

---

## 5. DETERMINISTIC PROOF & DEFINITION OF DONE (DoD)
- [ ] `theses/THESIS_024_TREE_OF_THOUGHTS_PRM.md` verified UTF-8 No-BOM.
- [ ] Zero-code pure NLP compliance maintained across repository.
- [ ] Isolated branch `student/node-024/thesis-tree-of-thoughts` merged into `main` via `--no-ff`.
- [ ] `registry/graduates.json` augmented with `node-024` accreditation record (70/30 attribution ratio).
- [ ] `README.md` version bumped to `v2.12.0`.
- [ ] Official Git tag `v2.12.0` created and verified.
- [ ] Downstream `acme-incubator` referee gate (`python verify.py`) passes 6/6 `PASS`.

---

## 6. VALUE ATTRIBUTION
* **Candidate Share:** 70% (`node-024`)
* **Curriculum Root Share:** 30% (`faculty-systems`)