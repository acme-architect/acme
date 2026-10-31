# THESIS SPEC: BILATERAL CONSTRAINT SATISFACTION & FLUFF-FREE ASSET MATCHING (RFC-035)
> **Candidate Node:** node-042  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/full-sweep/thesis-crucible-pipeline`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.22.0  
> **Constitutional Anchor:** CONSTITUTION.md Section I (Principle of Least Action), Section II (Dewdrop Boundary Invariant)

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), and Section II, Article 8 (Cryptographic Non-Repudiation).
* **Problem Formulation (Vanity Fluff Contamination & Asymmetric Brokerage Friction):** Distributed economic transaction networks suffer from massive communicative entropy, asymmetric information gatekeeping, and unverifiable cosmetic vanity claims (promotional marketing superlatives and stale phantom listings). Intermediaries waste substantial computational and human energy negotiating unstructured, uncalibrated descriptions. A cognitive matching engine must deconstruct incoming asset specifications and acquisition mandates into immutable, fluff-free scalar dimensions, verifying bilateral boundary constraints deterministically without conversational friction.
* **Negative Boundary Condition (Via Negativa):** Admitting unverified promotional superlatives into asset schemas, evaluating bilateral compatibility via probabilistic sentiment scoring, or permitting unverified stale circular syndication is strictly prohibited (`REJECT_UNCONSTRAINED_MATCH`).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Vanity Fluff Contamination):** Unfiltered marketing adjectives leaking into asset schemas -> `[PROHIBITED]` All incoming descriptors must pass automated regex decompilation into measurable physical scalars (`INV-BILATERAL-01`).
* **FAILURE MODE 2 (Stale Circular Syndication):** Re-listing duplicated or expired transaction mandates -> `[PROHIBITED]` Mandates lacking verifiable timestamp non-repudiation trigger immediate quarantine (`INV-BILATERAL-03`).
* **FAILURE MODE 3 (Probabilistic Matching Incoherence):** Scoring bilateral alignment via fuzzy qualitative heuristics -> `[PROHIBITED]` Bilateral matching must evaluate strictly as a deterministic Boolean Constraint Satisfaction Problem (`INV-BILATERAL-02`).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Vanity Fluff Decompilation** | **$\text{DoF} = 0$** | *Absolute Lex* | Unverified marketing adjectives are stripped to pure scalar metrics (`INV-BILATERAL-01`). |
| **Deterministic CSP Matching** | **$\text{DoF} = 0$** | *Integrity Lex* | Matching evaluates via hard Boolean boundary intersection; fuzzy sentiment barred. |
| **Stale Inventory Quarantine** | **$\text{DoF} = 0$** | *Boundary Lex* | Circular re-listings or expired mandates trigger immediate quarantine (`StaleListingError`). |
| **Machine-Verifiable Manifests** | **$\text{DoF} = 0$** | *Absolute Lex* | Transaction interfaces operate exclusively via structured schemas; free-text loops barred. |
| **Valuation Variance Margins** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Tolerance bands calibrate dynamically according to macro-market volatility indicators. |
| **Spatial Proximity Topologies** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Reachability isochrones adapt based on localized transport network telemetry. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INV-BILATERAL-01 (Vanity Fluff Decompilation):** Raw asset inputs must be stripped of all subjective, unverified promotional adjectives prior to ingestion. The resulting schema must consist strictly of measurable scalar dimensions and verified legal encumbrance states.
* **INV-BILATERAL-02 (Deterministic Bilateral Spec Matching):** Bilateral matching between asset specifications and acquisition mandates must execute as a deterministic Constraint Satisfaction Problem (CSP). Matching evaluates via Boolean boundary intersection:
  $$\text{Match}(\text{Asset}, \text{Mandate}) = \bigwedge_{i=1}^n \left( \text{Dim}_i(\text{Asset}) \cap \text{Bounds}_i(\text{Mandate}) \neq \emptyset \right)$$
  Probabilistic sentiment scoring is strictly prohibited.
* **INV-BILATERAL-03 (Stale Inventory & Phantom Mandate Quarantine):** Listings circulating across intermediary networks without active biological signatures or verified expiration timestamps are quarantined immediately to prevent phantom syndication loops.
* **INV-BILATERAL-04 (Machine-Verifiable Bilateral Contract Manifest):** Transaction parameters must serialize into structured, cryptographically signed JSON manifests, eliminating conversational natural-language re-negotiation.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Variance Headroom Boundary):** Price and valuation tolerance bounds should restrict divergence to $\le 10\%$ of median market benchmark indexes.
* **NORM 2 (Constraint Pruning Precedence):** When resolving over-constrained bilateral queries, non-load-bearing aesthetic parameters relax prior to core budgetary or dimensional invariants.

---

## 5. DEFINITION OF DONE (DoD)
- [ ] assert INV-BILATERAL-01 vanity fluff decompilation verified == True
- [ ] assert INV-BILATERAL-02 deterministic bilateral matching verified == True
- [ ] assert INV-BILATERAL-03 stale inventory quarantine verified == True
- [ ] assert INV-BILATERAL-04 machine-verifiable manifest verified == True
- [ ] assert verify.py exit code == 0
- [ ] assert git working tree verified pristine == True
