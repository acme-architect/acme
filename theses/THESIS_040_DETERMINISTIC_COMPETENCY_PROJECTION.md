# THESIS SPEC: DETERMINISTIC COMPETENCY PROJECTION & PRIVACY SHIELDING (RFC-024-B)
> **Candidate Node:** node-040  
> **Faculty:** faculty-law  
> **Target Branch:** `student/full-sweep/thesis-crucible-pipeline`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.22.0  
> **Constitutional Anchor:** CONSTITUTION.md Section II (Dewdrop Boundary Invariant & Biological Primacy)

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section II, Article 4 (Dewdrop Boundary Invariant), Section II, Article 7 (Biological Primacy), and Section II, Article 8 (Cryptographic Non-Repudiation).
* **Problem Formulation (Capability Hallucination & Identity Data Exposure):** Autonomous identity and competency projection systems degrade when probabilistic models hallucinate ungrounded credentials, inflate experience nodes absent from verified records, or broadcast sensitive personal identifiers across untrusted evaluation networks. Manual cross-referencing introduces severe cognitive churn, while unconstrained generative tailoring erodes cryptographic truth.
* **Negative Boundary Condition (Via Negativa):** Injecting unverified capability claims absent from the sealed root profile, evaluating requirement match via non-deterministic sentiment, or transmitting unmasked national identifiers and physical location coordinates is strictly prohibited (`REJECT_UNANCHORED_PROJECTION`).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Ungrounded Capability Embellishment):** Generative fabrication of unverified framework proficiencies or certifications -> `[PROHIBITED]` All projected competence records must be strict mathematical subsets of an immutable root profile.
* **FAILURE MODE 2 (Sensitive Identity Data Leakage):** Exposing national identification numbers, birthdates, or precise residential coordinates -> `[PROHIBITED]` Sensitive identity fields must undergo automated data minimization and cryptographic masking.
* **FAILURE MODE 3 (Probabilistic Matching Incoherence):** Scoring candidate capability fit using uncalibrated qualitative prose -> `[PROHIBITED]` Requirement alignment must evaluate deterministically via set intersection into discrete matched and gap vectors.

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Root Profile Immutability** | **$\text{DoF} = 0$** | *Lex Invariant* | Master profile is SHA-256 anchored. Unverified assertion triggers `UngroundedCapabilityInflationBreach`. |
| **Deterministic Set Matching** | **$\text{DoF} = 0$** | *Absolute Lex* | Requisition fit evaluates exclusively via exact set operations (`MATCHED`, `GAP`, `BONUS`). |
| **Privacy Data Masking** | **$\text{DoF} = 0$** | *Integrity Lex* | National identification numbers, residential coordinates, and demographic markers must be masked. |
| **Subset Projection Parity** | **$\text{DoF} = 0$** | *State Invariant* | Tailored representations must be strict mathematical subsets of verified master competence. |
| **Stylistic Formatting Adaptation**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Output layout schemas (Markdown, JSON, text) adapt dynamically to client consumer parsers. |
| **Ontological Synonym Mapping** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Verified technical aliases resolve via deterministic, approved synonym dictionaries. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INV-COMP-01 (Immutable Root Profile):** The primary competence profile is an immutable, cryptographically sealed record. Generating or emitting capabilities not explicitly verified within the root profile is barred via `UngroundedCapabilityInflationBreach`.
* **INV-COMP-02 (Deterministic Requirement Scoring):** Target criteria must evaluate against the master profile via Boolean set algebra, partitioning dimensions into `MATCHED`, `GAP`, and `BONUS` vectors with objective percentage coverage metrics.
* **INV-COMP-03 (Subset Projection Parity):** Every generated variant must be a strict homomorphic projection of the master profile, prioritizing verified experiences that directly satisfy target criteria while pruning unaligned noise.
* **INV-COMP-04 (Privacy Minimization Shield):** Primary identifiers including national registration numbers, residential street addresses, and demographic attributes must be redacted by default, exposing only authorized professional interfaces and verifiable cryptographic diplomas.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Layout Format Elasticity):** Document section structure and serialization schemas may adapt to match external automated parsing engines without altering underlying semantic facts.
* **NORM 2 (Competency Density Tuning):** Presentation variants should constrain experience descriptions to the top three highest-resonance evidence nodes per target requirement.

---

## 5. DEFINITION OF DONE (DoD)
- [ ] assert INV-COMP-01 immutable root profile verified == True
- [ ] assert INV-COMP-02 deterministic requirement scoring verified == True
- [ ] assert INV-COMP-03 subset projection parity verified == True
- [ ] assert INV-COMP-04 privacy minimization shield verified == True
- [ ] assert verify.py exit code == 0
- [ ] assert git working tree verified pristine == True
