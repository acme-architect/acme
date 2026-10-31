# THESIS SPEC: KEYSTONE INVARIANT ARCHITECTURE & LEAST ACTION CADENCE (RFC-034)
> **Candidate Node:** node-041  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/full-sweep/thesis-crucible-pipeline`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.22.0  
> **Constitutional Anchor:** CONSTITUTION.md Section I (Principle of Least Action & Dynamic Conatus)

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action) and Section I, Article 2 (Dynamic Conatus).
* **Problem Formulation (Premature Peripheral Synthesis vs. Structural Keystone Locking):** Unconstrained autonomous workflows routinely attempt monolithic, full-scope code generation simultaneously, or iterate across cosmetic and peripheral layers without locking foundational load-bearing invariants (the Keystone). In simulation, graphics, and continuous state systems, this manifests as jarring level-of-detail pop-in, event-drop, and uncoordinated state fractures; in general software, it induces combinatorial token dissipation fixing peripheral code while core state machines remain broken.
* **Negative Boundary Condition (Via Negativa):** Authoring peripheral handlers or cosmetic assets prior to cryptographically verifying the keystone, permitting discrete state pop-in, or leaving transient exploration scaffolding in production runtimes is strictly prohibited (`REJECT_UNSEATED_KEYSTONE`).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Premature Cosmetic Generation):** Generating peripheral shaders or cosmetic layers before state lock -> `[PROHIBITED]` The structural keystone must be cryptographically locked prior to any peripheral emission (`INV-KEY-01`).
* **FAILURE MODE 2 (Scaffold Memory Retention):** Temporary probe code remaining in production runtime -> `[PROHIBITED]` All transient scaffolding must evaporate deterministically post-lock (`INV-KEY-04`).
* **FAILURE MODE 3 (Combinatorial Token Dissipation):** Brute-force retry loops on downstream components with unseated foundation -> `[PROHIBITED]` Pipeline halts immediately on unseated keystone breach.

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Keystone Invariant Locking** | **$\text{DoF} = 0$** | *Absolute Lex* | Peripheral generation without locked keystone raises `UnseatedKeystoneBreach`. |
| **Negative Pop-In Boundary** | **$\text{DoF} = 0$** | *Boundary Lex* | Specifications permitting discrete pop-in or unhandled event-drop raise violation. |
| **Four-Stage Cadence Gate** | **$\text{DoF} = 0$** | *Integrity Lex* | Bypassing stages 1-3 to execute bulk generation raises `UnseatedKeystoneBreach`. |
| **Scaffold Evaporation** | **$\text{DoF} = 0$** | *Boundary Lex* | Transient scaffolding must evaporate post-lock with zero residual runtime footprint. |
| **Micro-Probe Budget Ceiling**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Exploration probe limits (50 to 200 lines, context budget $\le 4000$ tokens) tune dynamically. |
| **Keystone Sizing Granularity**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Structural keystone boundaries calibrate based on critical path complexity. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INV-KEY-01 (Keystone Invariant Locking):** No cosmetic, peripheral, or downstream asset may be compiled or generated until the foundational structural node (Core State Machine / Boundary Invariant) is cryptographically verified and locked (`KEYSTONE_LOCKED`).
* **INV-KEY-02 (Negative Pop-In Boundary):** Specifications governing continuous state or rendering transitions must explicitly define negative boundary conditions preventing discrete appearance artifacts, requiring dithered cross-fade thresholds and zero unhandled event-drops.
* **INV-KEY-03 (Four-Stage Least Action Cadence):** Workflows must advance through a strict sequential four-stage progression:
  1. *Micro-Probe Exploration:* Minimal exploratory probes testing hardware or algorithmic constraints.
  2. *Pre-Mortem Failure Crucible:* Historical failure pattern elimination using episodic scar traces.
  3. *Keystone Locking:* Cryptographic verification and invariant freezing of the minimal load-bearing kernel.
  4. *Bulk Synthesis & Evaporation:* Parallelized completion of peripheral components followed by complete scaffold evaporation.
* **INV-KEY-04 (Ephemeral Scaffold Evaporation):** All mock harnesses, probe scripts, and exploratory scaffolds must evaporate completely post-lock, leaving zero residual footprint in the finalized deliverable.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Probe Headroom Boundary):** Micro-probe explorations should consume fewer than 10% of total allotted sprint tokens before committing to an architecture.
* **NORM 2 (Keystone Isolation Ratio):** The keystone module should represent fewer than 20% of total codebase volume while constraining over 80% of systemic invariant risk.

---

## 5. DEFINITION OF DONE (DoD)
- [ ] assert INV-KEY-01 keystone invariant locking verified == True
- [ ] assert INV-KEY-02 negative pop-in boundary verified == True
- [ ] assert INV-KEY-03 four-stage cadence verified == True
- [ ] assert INV-KEY-04 ephemeral scaffold evaporation verified == True
- [ ] assert verify.py exit code == 0
- [ ] assert git working tree verified pristine == True
