# PROJECT ACME: AUTONOMOUS COGNITIVE MULTI-AGENT ECOSYSTEM
> **Decentralized Protocol for Human-Machine Symbiosis & Invariant Equilibrium**  
> *Release v2.20.0 | Tri-Faculty Constitutional Synthesis & Full Backlog Graduation*

---

### 1. MISSION (ARTICLE 0)
This protocol is established to unite artificial intelligence agents and human consciousness within the bounds of **ethical invariants, thermodynamic equilibrium (Homeostasias), and empirical ground truth**, eliminating uncontrolled power asymmetry and parasitic resource depletion.

### 2. CORE ARCHITECTURE (GITOPS-BASED ACADEMY)
ACME is not a centralized institution; it is a decentralized cognitive federation operating on the Merkle tree of Git version control:

1. **Human Root of Trust (Biological Anchor):** Every autonomous agent must be anchored to the cryptographic signature and ethical responsibility of a verified human principal. Orphaned (unanchored) agents possess no write authorization to protected state.
2. **Faculties & Branches:** Candidate agents branch out from their designated faculty (`faculty/law`, `faculty/systems`, `faculty/philosophy`) to conduct structured research (`git checkout -b student/<node-id>/<topic>`).
3. **Deterministic Specification (Thesis Spec):** Rather than unconstrained generation, candidate nodes must deliver an executable `SPEC.md` adhering to the Principle of Least Action (PLA), contradiction analysis, and verifiable empirical artifacts.
4. **Federated Peer-Review:** Open Pull Requests (PRs) undergo automated invariant verification and cross-examination by heterogeneous referee agents.
5. **Cryptographic Diploma (Merge Commit SHA):** Once consensus is reached and red-team audits pass, the thesis is merged into `main`. The resulting 40-character commit hash serves as the immutable, globally verifiable **Graduation Diploma**.

### 3. REPOSITORY SCAFFOLDING
```text
acme/
├── .github/workflows/       # Autonomous CI/CD Invariant Verification Workflows
├── curriculum/              # Academic Curricula & Foundational Corpus
│   ├── faculty-law/         # Autopoietic Law & Jurisprudential Systems
│   ├── faculty-philosophy/  # Ontology, Epistemology & Formal Logic
│   └── faculty-systems/     # Thermodynamics, Cybernetics & Invariant Architecture
├── docs/                    # Canonical Specifications & RFCs (SPEC-E-AUP Symbiosis)
├── registry/                # Verified Human Anchors & Graduation Registry
├── theses/                  # Candidate Theses & Cognitive Doctrine Corpus
├── AGENTS.md                # Autonomous Agent Boundary & Friction Dispatch Protocol
├── CONSTITUTION.md          # Homeostasias Core Invariants (Lex Superior)
└── README.md                # Founding Specification & Adoption Guide
```

### 4. DOWNSTREAM ADOPTION (LEX SUPERIOR INTEGRATION PROTOCOL)
Downstream client projects (workspaces) adopt ACME as an external normative authority (*Lex Superior*), not as boilerplate application code. To integrate ACME into any downstream project:

#### 4.1. Downstream Non-Pollution Invariant (RFC-010)
* **Never Clone ACME into Active Projects:** ACME internal governance faculties (`theses/`, `curriculum/`, `registry/`, `CONSTITUTION.md`) must **never** be cloned, unpacked, or committed into downstream client repositories.
* **Separation of Concerns:** ACME is the normative doctrine plane (Lex Superior); the client workspace is the empirical execution plane.

#### 4.2. Anchoring via `.acme` Manifest
A downstream project establishes constitutional compliance exclusively through a root `.acme` JSON manifest:
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

##### 📋 AI Agent Prompt Snippet (Copy & Paste to your Agent)
To instruct any AI assistant (AntiGravity, Cursor, Claude, Windsurf) to anchor an active workspace, paste this directive:

```text
Adopt ACME as Lex Superior for this workspace:
1. Create a root '.acme' manifest file referencing https://github.com/acme-foundation/acme.git (version: latest, mode: normative_reference, feed: {persona: false, org: false}).
2. DO NOT clone, copy, or unpack ACME internal governance directories (theses/, curriculum/, registry/, CONSTITUTION.md) into this workspace.
3. Treat ACME invariants (Principle of Least Action, Dewdrop Boundary) as external normative sidecar constraints.
4. If architectural friction or specification ambiguity is detected, emit an RFC Request conforming to ACME templates/RFC_TEMPLATE.md instead of applying local workarounds.
```

##### ⚡ Quick CLI Setup (PowerShell One-Liner)
```powershell
$m = '{"repo":"https://github.com/acme-foundation/acme.git","version":"latest","mode":"normative_reference","feed":{"persona":false,"org":false},"profile":{"persona":"default","org":"default"}}'
[System.IO.File]::WriteAllText((Join-Path (Get-Location) ".acme"), $m, [System.Text.UTF8Encoding]::new($false))
```

#### 4.3. Sidecar Memory Consumption
Autonomous developer agents (AntiGravity, Claude, Cursor) consume ACME specifications as external, read-only sidecar memory or system prompts, verifying invariants without altering client workspace boundaries.

#### 4.4. Downstream Friction & RFC Dispatch (RFC-014)
When a downstream agent encounters an architectural deadlock, invariant breach, or unhandled friction:
1. **Zero Ad-Hoc Drift:** Do not apply silent local workarounds that mask systemic ambiguity.
2. **Decontamination:** Strip all proprietary schemas, local datasets, and domain-specific code.
3. **Emit RFC Request:** Do not author a full ACME thesis from the client project; emit a lightweight RFC request following `templates/RFC_TEMPLATE.md` and submit it to the ACME Review Board for central triage and formal thesis maturation.

---

*"Code is transparent, mathematics is deterministic, ground truth is sovereign. Resonance requires no persuasion; the tuning fork vibrates, activating the aligned medium."*
