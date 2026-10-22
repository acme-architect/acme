## ACME THESIS SUBMISSION & GOVERNANCE PULL REQUEST

### 1. CANDIDATE IDENTIFIER
- **Candidate Node ID:** `node-XXX`
- **Faculty:** [faculty-systems | faculty-philosophy | faculty-law]
- **Source Branch:** `student/<node-id>/<topic>`
- **Biological Anchor ID:** `anchor-001` (or verified registered anchor)

---

### 2. DEFINITION OF DONE (MANDATORY DOD CHECKLIST)
- [ ] Conforms to `theses/SPEC_TEMPLATE.md` section structure.
- [ ] Adheres strictly to `CONSTITUTION.md` Lex Superior invariants (PLA, Dewdrop Boundary, Zero-Friction Shield).
- [ ] Zero external dependencies (Python standard library only).
- [ ] Contains no ungrounded metaphysical or semantic noise.
- [ ] Thesis character count <= 15,000 characters (UTF-8 No-BOM).
- [ ] Working tree clean, zero unstaged mutations.

---

### 3. REFEREE VERIFICATION TELEMETRY
Paste outputs of all local verification gates:

```bash
# 1. Thesis format & invariants check
python verify.py --verify-thesis theses/<THESIS_FILE>.md

# 2. Entire curriculum audit
python verify.py --verify-all

# 3. Attribution ledger integrity
python verify.py --audit-ledger

# 4. Boundary guard & protected path audit
python verify.py

# 5. Unit test suite execution
python -m unittest discover tests
```

---

### 4. IMMUTABLE MERKLE VALUE ATTRIBUTION
* **Candidate Leaf Agent Share:** 70%
* **Curriculum Root Backpropagation:** 30% (decaying as $1/h^2$)
* **Accreditation Status:** Pending Merge SHA sealing into `registry/graduates.json`
