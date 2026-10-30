# AGENTS.md — ACME Ecosystem Execution Protocol for AI Agents

## 1. Scope & Execution Boundary
When an operator requests to develop a project "using ACME", "compliant with ACME", or commands to "Update ACME":
1. **NEVER Clone or Checkout ACME into the Active Project Workspace:** ACME is an external cognitive constitution (Lex Superior), not application boilerplate.
2. **Context Memory & Sidecar:** Always fetch or reference ACME as an external, read-only normative specification or sidecar memory.
3. **Workspace Sanitization:** Keep the user's project workspace 100% free of ACME internal administrative structures (`curriculum/`, `theses/`, `registry/`).
4. **Downstream Manifest:** Identify compliant projects exclusively via the presence of a root `.acme` manifest file.

## 2. Downstream Friction & RFC Reporting Protocol
When working inside a downstream client workspace:
1. **DO NOT** attempt to author a full ACME thesis from the client project.
2. If architectural friction or missing constraints are detected, emit an RFC Request conforming to `templates/RFC_TEMPLATE.md`.
3. Submit the request to the ACME Review Board for triage, aggregation, and formal thesis maturation.

## 3. Scale Invariance & Pre-Mortem Anti-Pattern Protocol (THESIS-036)
When drafting living specifications (`specs/`):
1. **Micro-Macro Failure Isomorphism:** Autonomous agents must evaluate state machines for scale-invariant failure modes (e.g., buffer exhaustion, race conditions, cyclic deadlocks).
2. **Mandatory Known Failure Mode Catalog:** Every specification MUST explicitly catalog the top 3 domain-specific failure modes before construction.
3. **Pre-Mortem Anti-Pattern Gate (DoF = 0):** Specifications MUST include a dedicated section `### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)` prohibiting these modes via hard negative constraints (`[PROHIBITED]`). Specifications lacking this gate fail pre-flight verification immediately (`REJECT_UNANCHORED_INCEPTION`).
