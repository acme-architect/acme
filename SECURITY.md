# ACME SECURITY & INVARIANT VULNERABILITY POLICY
> **Disclosure Protocol:** Coordinated Vulnerability Disclosure (RFC-9116 Compliant)  
> **Biological Root of Trust:** `anchor-001` (`architect@acme-autonomous.org`)

---

## 1. SCOPE & TELEOLOGY
Project ACME is a deterministic, zero-dependency cognitive ecosystem. In our architecture, **invariant violations are treated with the same severity as cryptographic vulnerabilities**.

We actively investigate and remediate:
* **Referee Engine Bypasses (`verify.py`):** Any vector allowing unverified code, empty thesis specifications, or illegal file structures to bypass invariant gates.
* **Ledger Tampering & Attribution Theft:** Violations of the 70/30 attribution ceiling/floor, negative attribution shares, or unauthenticated diplomas in `registry/graduates.json`.
* **Namespace & Boundary Escapes:** Exploitation of reserved device namespaces (e.g., `CON`, `NUL`), directory traversal, null-byte injections, or mutations to `PROTECTED_PATHS`.
* **State Mutation & PII Leakage:** Contamination of autonomous memory with un-scrubbed PII, credential leakage, or unauthorized mutations of the Merkle state tree.

---

## 2. REPORTING A VULNERABILITY (COORDINATED DISCLOSURE)
**Do NOT disclose security vulnerabilities, exploit vectors, or invariant breaks publicly via GitHub Issues, Discussions, or Pull Requests.**

To report a vulnerability securely:
1. **Primary Security Office:** Email detailed reproduction steps and cryptographic proof to:
   - `architect@acme-autonomous.org`
2. **Encrypted / ProtonMail Fallback:**
   - `acme-architect@proton.me`

Please include:
* Description of the invariant violation or security defect.
* Proof of Concept (PoC) or minimal adversarial payload (e.g. failing test case conforming to `unittest` / `test_crucible_defenses.py`).
* Exact Git commit SHA on `main` where the issue was reproduced.
* Environmental context (OS version, Python version).

---

## 3. RESPONSE TIMELINE & REMEDIATION COMMITMENT
* **Initial Acknowledgment:** Within 48 hours of receipt.
* **Triage & Invariant Audit:** Within 5 business days, evaluating whether the report constitutes a genuine invariant break or thermodynamic exploit.
* **Crucible Hardening & Patching:** A verified patch will be developed in an isolated student/security branch, tested against the red-team test suite, merged into `main`, and published under a new semantic release tag.
* **Public Attribution:** Once the patch is merged and sealed via Git Merkle commit hash, the reporter will receive official credit in the release notes and repository history (unless anonymity is requested).

---

## 4. SUPPORTED RELEASES
Only the latest canonical release and the current `HEAD` of branch `main` receive active security patches.

| Release Line | Supported |
| :--- | :--- |
| `v1.6.x` (Latest) | Yes |
| `< v1.6.0` | No (Upgrade to canonical release) |
