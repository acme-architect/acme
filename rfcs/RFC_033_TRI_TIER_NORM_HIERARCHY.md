# RFC REQUEST: TRI-TIER NORM HIERARCHY & DOUBLE INVARIANT PRE-FLIGHT GATE
> **Reporting Client / Node:** acme-downstream-client  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-systems / faculty-law  
> **Anchored Theses:** THESIS-003, THESIS-016, THESIS-031, THESIS-034  

---

## 1. OBSERVED FRICTION (WHAT BROKE?)
- **Context:** Autonomous developer agents and downstream project teams jump directly from tacit, adjective-laden user prompts into code synthesis without operational grounding.
- **Root Tension:**
  1. Uncalibrated subjective adjectives (*"fast"*, *"modern"*, *"clean"*, *"secure"*, *"high-performance"*) grant unconstrained degrees of freedom ($\text{DoF} \to \infty$) to the generative model, causing massive semantic drift and hallucination.
  2. Specifications author features in conflict with either local hardware/domain constraints or universal constitutional invariants due to the absence of a verified, stratified hierarchy.

---

## 2. AD-HOC WORKAROUND (HOW WAS WORK PRESERVED?)
- **Immediate Mitigation:** Ad-hoc manual code review, post-generation refactoring sprints, and conversational prompting to correct drifted code.
- **Residual Risk:** Severe context contamination, non-deterministic compiler failures, cognitive burnout, and systemic architectural erosion.

---

## 3. PROPOSED HYPOTHESIS & DUAL SPECIFICATION

### A. Proposed Lex (Hard Invariants, DoF = 0)
* **INV-NORM-01 (Three-Tier Norm Hierarchy):** Normative authority follows strict unidirectional precedence:
  $$\text{Layer 1: CONSTITUTION.md (Lex Superior)} \succ \text{Layer 2: .acme/PROJECT\_INVARIANTS.md (Lex Specialis)} \succ \text{Layer 3: specs/SPEC\_*.md (Lex Executiva)}$$
* **INV-NORM-02 (Double Invariant Gate):** A specification cannot proceed to the Construction phase unless it simultaneously fulfills:
  $$\text{Compilation Approval} \iff (\text{SPEC} \models \text{PROJECT\_INVARIANTS}) \land (\text{PROJECT\_INVARIANTS} \models \text{CONSTITUTION})$$
  Any conflicting assertion across tiers triggers immediate evaluation rejection (`REJECT_UNALIGNED_SPEC`).
* **INV-NORM-03 (Banned Fluff Adjective Filter):** Raw adjectives lacking operational definitions (e.g., *fast, modern, scalable, elegant, robust, secure*) are banned from passing intake. The pre-flight gate halts execution (`STATUS: HOLD/HALT`).
* **INV-NORM-04 (Mandatory Via Negativa & Binary DoD):** Every specification must explicitly contain:
  1. An explicit `## VIA NEGATIVA` or `## INVARIANTS` section defining prohibited state transitions ($\text{DoF}=0$).
  2. A Definition of Done (DoD) consisting strictly of binary mathematical assertions (`assert`, `exit code`, `SHA-256`, `P95 latency <=`, `==`, `>=`).

### B. Proposed Norms (Adaptive Guidance, DoF >= 1)
* **Pre-Flight Circuit Breaker (`referee.py`):** Standalone zero-dependency scanner executed before code generation begins.
* **Deterministic Remediation Protocol:** When tripped, the circuit breaker emits unambiguous remediation mandates directing the author to ground tacit claims into mathematical metrics before retrying.
