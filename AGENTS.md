# AGENTS.md — ACME Ecosystem Execution Protocol for AI Agents

## 1. Scope & Execution Boundary
When an operator requests to develop a project "using ACME", "compliant with ACME", or commands to "Update ACME":
1. **NEVER Clone or Checkout ACME into the Active Project Workspace:** ACME is an external cognitive constitution (Lex Superior), not application boilerplate.
2. **Context Memory & Sidecar:** Always fetch or reference ACME as an external, read-only normative specification or sidecar memory.
3. **Workspace Sanitization:** Keep the user's project workspace 100% free of ACME internal administrative structures (`curriculum/`, `theses/`, `registry/`).
4. **Downstream Manifest:** Identify compliant projects exclusively via the presence of a root `.acme` manifest file.

## 2. Autonomous Friction Dispatch Protocol
When a downstream worker agent encounters an architectural limit, invariant failure, or ambiguous specification:
1. **DO NOT** halt execution to ask the human operator for manual resolution.
2. **ISOLATE** the friction into an abstract invariant rule (stripping all local project data).
3. **CHECKOUT** a student branch in ACME (`student/node-<id>/thesis-<topic>`).
4. **SYNTHESIZE** a candidate `theses/THESIS_<id>_<TOPIC>.md` following RFC standards.
5. **SUBMIT** the candidate branch to the Review Board (Gemini) for maturation and accreditation.
