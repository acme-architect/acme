# THESIS SPEC: TRI-TIER CONTEXT FABRIC, SINGLE MANIFEST & PRE-FLIGHT CIRCUIT BREAKER (RFC-033)
> **Candidate Node:** node-037  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/full-sweep/thesis-crucible-pipeline`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.22.0  
> **Constitutional Anchor:** CONSTITUTION.md Section II (Dewdrop Boundary Invariant & Biological Primacy)

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), and Section II, Article 7 (Biological Primacy).
* **Problem Formulation (Fragmented Context & Unchecked Telemetry Bleed):** Multi-agent downstream workspaces suffer from configuration fragmentation when governance, organization, and persona settings scatter across uncoordinated root dotfiles (`.org`, `.persona`, `.acme-config`). Furthermore, default-open telemetry architectures silently leak developer heuristics, source code, and enterprise intellectual property into external model context windows. Finally, allowing code generation from ungrounded user prompts without pre-flight verification induces massive downstream rework.
* **Negative Boundary Condition (Via Negativa):** Scattering configuration across multiple root files, exfiltrating context telemetry without affirmative human authorization, or executing construction workflows without passing the pre-flight circuit breaker is strictly prohibited (`REJECT_UNANCHORED_INCEPTION`).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Configuration Fragmentation):** Generating multiple ad-hoc root configuration dotfiles -> `[PROHIBITED]` All project configuration must reside exclusively in the single root `.acme` manifest (`INV-SINGLE-MANIFEST`).
* **FAILURE MODE 2 (Silent Telemetry Exfiltration):** Default-open transmission of local workspace data or developer persona traces -> `[PROHIBITED]` Telemetry and context ingestion default unconditionally to deny (`INV-OPTIN-STRICT`).
* **FAILURE MODE 3 (Fluff-Ridden Unanchored Construction):** Compiling code from specifications containing uncalibrated subjective adjectives -> `[PROHIBITED]` Specifications must pass the pre-flight circuit breaker verifying 3-tier hierarchy and binary mathematical DoD assertions.

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Single Manifest Invariant** | **$\text{DoF} = 0$** | *Lex Invariant* | Presence of extraneous root configuration files halts execution immediately (`INV-SINGLE-MANIFEST`). |
| **Default-Deny Context Shield** | **$\text{DoF} = 0$** | *Absolute Lex* | Context transmission flags default to false. Transmission without biological signature raises violation. |
| **Pre-Flight Circuit Breaker** | **$\text{DoF} = 0$** | *Integrity Lex* | Spec lacking 3-tier grounding or containing fluff triggers immediate circuit trip (`HOLD/HALT`). |
| **Persona Stylistic Heuristics**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Personal prompt styles and interaction cadence adapt freely within the bounded persona tier. |
| **Organizational SOP Sizing** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Enterprise compliance policies dynamically configure verification depths and audit log retention. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INV-SINGLE-MANIFEST (Single Root Manifest):** Workspaces are prohibited from generating multiple root configuration dotfiles. All bindings must reside in the single `.acme` JSON manifest at the repository root.
* **INV-OPTIN-STRICT (Default-Deny Context Shield):** Context flags `feed.persona` and `feed.org` must default to `false`. Without explicit biological authorization, zero local source code, heuristics, or telemetry may cross boundary membranes.
* **INV-PREFLIGHT-SWOT (Pre-Flight Circuit Breaker Gate):** No task specification may proceed to code construction without passing the automated pre-flight gate. The circuit breaker asserts:
  1. Full compliance with the 3-Tier Norm Hierarchy (`SPEC` $\models$ `PROJECT_INVARIANTS` $\models$ `CONSTITUTION`).
  2. Complete elimination of ungrounded subjective descriptors.
  3. Explicit negative boundary constraints (`## VIA NEGATIVA` or `## INVARIANTS`).
  4. Binary mathematical assertions in the Definition of Done.
* **INV-TRI-TIER-PRECEDENCE (Normative Precedence Hierarchy):** Governance follows a strict unidirectional hierarchy:
  $$\text{Tier 3 (Persona)} \models \text{Tier 2 (Corporate Specialis)} \models \text{Tier 1 (Foundation Superior)}$$
  Lower tiers cannot override constraints defined by higher tiers.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Canonical Manifest Schema):** Standard `.acme` schema groups configuration within single-depth namespaces (`feed`, `profile`, `repo`, `mode`).
* **NORM 2 (Subordination Dispute Resolution):** Conflicting assertions between persona preferences and corporate invariants resolve automatically in favor of the higher normative tier with diagnostic warning logging.

---

## 5. DEFINITION OF DONE (DoD)
- [ ] assert INV-SINGLE-MANIFEST root manifest uniqueness verified == True
- [ ] assert INV-OPTIN-STRICT default-deny context shield verified == True
- [ ] assert INV-PREFLIGHT-SWOT circuit breaker pre-flight gate verified == True
- [ ] assert INV-TRI-TIER-PRECEDENCE normative hierarchy verified == True
- [ ] assert verify.py exit code == 0
- [ ] assert git working tree verified pristine == True
