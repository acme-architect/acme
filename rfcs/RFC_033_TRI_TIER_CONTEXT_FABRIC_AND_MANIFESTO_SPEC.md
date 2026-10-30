# RFC REQUEST: TRI-TIER CONTEXT FABRIC, SINGLE .ACME MANIFESTO & PRE-FLIGHT H-SWOT GATE (RFC-033)
> **Reporting Client / Node:** acme-downstream-client  
> **Status:** RATIFIED_SPEC  
> **Target Faculty:** faculty-systems / faculty-law  
> **Target Release:** ACME v2.21.0  
> **Anchored Theses:** THESIS-003, THESIS-010, THESIS-016, THESIS-020, THESIS-031, THESIS-034  

---

## 1. CONSTITUTIONAL H-SWOT AUDIT & ARCHITECTURAL JUSTIFICATION
Prior to this specification, an internal Holographic SWOT (H-SWOT) interferometer audit of `CONSTITUTION.md` revealed critical epistemic vulnerabilities:
- **Article 2 (Dynamic Conatus):** Allowed potential scope evasion under the guise of "adapting boundary conditions".
- **Article 3 (Habitable Zone):** Lacked a deterministic operational threshold for over-engineering versus chaotic drift.
- **Article 5 (Observer Core):** Contained literary aphorisms (*"claims of absolute nothingness are mathematically undefined"*) permitting unbounded prompt drift ($\text{DoF} \to \infty$).
- **Article 6 (Zero-Friction Shield):** Risked being weaponized as a "black hole fallacy" to silently drop exceptions without audit trails.

Through Via Negativa refactoring ($\text{DoF} = 0$), these articles were hardened into explicit operational invariants:
- **Article 2:** `[PROHIBITED_LOCAL_MUTATION]` and `REJECT_SCOPE_EVASION`.
- **Article 3:** `[PROHIBITED_FROZEN_OR_CHAOTIC]` and a strict $\text{DoF} \le 1.5\times$ ceiling (`REJECT_EXTREME_ENTROPY`).
- **Article 5:** `[REJECT_SPECULATIVE_STATE]` and mandatory `HALT` with exit code 1.
- **Article 6:** `[PROHIBITED_SILENT_DROP]` and zero-token `QUARANTINE_AND_LOG`.

Building upon this constitutional equilibrium, **RFC-033** resolves downstream context leakage: preventing workspace root pollution from fragmented configuration files, securing personal and corporate privacy via default-deny context boundaries, and enforcing pre-flight circuit breaking prior to code generation.

---

## 2. INVIOLABLE INVARIANTS (THE LEX: DoF = 0)

* **INV-SINGLE-MANIFEST:** Downstream project workspaces are strictly prohibited from generating multiple root configuration files (`.org`, `.persona`, `.acme-config`, etc.). All normative, corporate, and individual profile bindings must reside exclusively inside the single `.acme` JSON manifest at the repository root.
* **INV-OPTIN-STRICT (Default-Deny Context Shield):** The context transmission flags `feed_persona` and `feed_org` MUST default to `false` (`Default-Deny`). In the absence of an explicit cryptographic/biological human signature and affirmative authorization, zero local source code, developer heuristics, or workspace telemetry may be dispatched to external memory pools or shared model context windows.
* **INV-PREFLIGHT-SWOT (Pre-Flight Circuit Breaker Gate):** No user intent or issue ticket may be converted into code construction without passing the H-SWOT pre-flight gate. The gate verifies:
  1. Full compliance with the 3-Tier Norm Hierarchy (`SPEC` $\models$ `PROJECT_INVARIANTS` $\models$ `CONSTITUTION`).
  2. Zero ungrounded subjective fluff adjectives (e.g., *fast, modern, scalable, secure, robust*).
  3. Explicit `## VIA NEGATIVA` or `## INVARIANTS` negative constraint section.
  4. Binary mathematical assertions in the Definition of Done (DoD).
* **INV-PURE-NLP:** All doctrinal specifications and constitutional core artifacts remain 100% pure Markdown/JSON, UTF-8 No-BOM, with zero executable code artifacts in the core repository.

---

## 3. TRI-TIER CONTEXT FABRIC ARCHITECTURE

Normative authority and context aggregation follow a strict three-tier unidirectional precedence hierarchy:

```text
               [TIER 1: ACME Foundation] (CONSTITUTION.md)
                      ▲  (Universal Law / Lex Superior / DoF = 0)
                      │
           [TIER 2: Corporate Profile] (.acme/PROJECT_INVARIANTS.md)
                      ▲  (Enterprise Domain SOP / Memory & Compliance / Lex Specialis)
                      │
           [TIER 3: Architect Persona] (persona_profile)
                         (Cognitive Style / Digital Twin Heuristics / Lex Personae)
```

1. **Tier 1 (ACME Foundation - Lex Superior):** Universal thermodynamic, cybernetic, and cognitive invariants. Non-negotiable, scale-invariant, cross-project authority.
2. **Tier 2 (Corporate Profile - Lex Specialis):** Domain constraints, hardware bounds, regulatory compliance (ISO 27001, NIS2), and organizational standard operating procedures (`org_profile`).
3. **Tier 3 (Architect Persona - Lex Personae):** Developer mental models, preferred refactoring patterns, and prompt interaction styles (`persona_profile`).

**Subordination Rule:** $\text{Tier 3} \models \text{Tier 2} \models \text{Tier 1}$. A developer persona cannot violate corporate constraints; corporate rules cannot violate ACME constitutional invariants. Any conflicting assertion halts execution with `REJECT_UNALIGNED_SPEC`.

---

## 4. CANONICAL DOWNSTREAM `.acme` MANIFEST SCHEMA (BEST PRACTICE)

Downstream projects implementing ACME bind their context exclusively through this root `.acme` manifest, adhering to single-depth hierarchical grouping ($\text{Depth} \le 1$):

```json
{
  "repo": "https://github.com/acme-foundation/acme.git",
  "version": "latest",
  "mode": "normative_reference",
  "feed": {
    "persona": false,
    "org": false
  },
  "profile": {
    "persona": "default",
    "org": "default"
  }
}
```

### Schema Block Definitions:
1. **Root Parameters (Technical Coordinates):**
   * `repo`: Cryptographic repository URI of the ACME normative core.
   * `version`: Release tag coordinate (e.g., `latest` or pinned `v2.20.2`).
   * `mode`: Operating posture (`normative_reference` for standard clients, `autonomous_workspace` for sovereign nodes).
2. **`feed` Block (Opt-In / Consent Shield - INV-OPTIN-STRICT):**
   * `persona`: Boolean (default `false`). When `false`, zero developer habits, keystrokes, or persona heuristics are exfiltrated.
   * `org`: Boolean (default `false`). When `false`, zero proprietary internal schemas, client code, or organizational memory are shared.
3. **`profile` Block (Identity Namespace):**
   * `persona`: Identifier for the isolated local digital twin profile (default `"default"`).
   * `org`: Identifier for the isolated enterprise compliance profile (default `"default"`).

*Backward Compatibility Note: Automated parsers normalize legacy flat keys (`acme_standard`, `feed_persona`, `feed_org`) into canonical grouped namespaces.*

---

## 5. PRE-FLIGHT CIRCUIT BREAKER PROTOCOL (`referee.py`)

Every autonomous agent or downstream development cycle executes the pre-flight circuit breaker prior to modifying the workspace working tree:

```powershell
python tools/referee.py --preflight-gate specs/SPEC_TARGET.md
```

### Audit Pipeline:
1. **Fluff Adjective Scan:** Scans for uncalibrated subjective descriptors (`banned_fluff`). Any match trips the breaker (`STATUS: HOLD/HALT`).
2. **Hierarchy Collision Audit:** Verifies that the spec does not breach `.acme/PROJECT_INVARIANTS.md` or `CONSTITUTION.md`.
3. **Via Negativa Verification:** Enforces explicit negative boundary documentation ($\text{DoF} = 0$).
4. **Binary DoD Certification:** Verifies that acceptance criteria evaluate to binary truth vectors (`assert`, `exit code`, `<=`, `==`, `>=`).

---

## 6. DEFINITION OF DONE (DoD)
- [ ] `rfcs/RFC_033_TRI_TIER_CONTEXT_FABRIC_AND_MANIFESTO_SPEC.md` formatted in UTF-8 No-BOM.
- [ ] `INV-SINGLE-MANIFEST` and `INV-OPTIN-STRICT` codified as absolute invariants ($\text{DoF} = 0$).
- [ ] Canonical JSON schema for `.acme` manifest documented and validated.
- [ ] Automated verification gate passes with zero errors (`exit code 0`).
- [ ] Git commit conforming to: `feat(rfcs): specify tri-tier context fabric, single .acme manifesto and H-SWOT preflight gate (RFC-033)`.
- [ ] Working tree clean (`git status` clean).
