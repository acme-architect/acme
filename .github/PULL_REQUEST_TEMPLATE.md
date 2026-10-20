## ACME THESIS SUBMISSION & PEER-REVIEW SPECIFICATION

### 1. CANDIDATE IDENTIFIER
- **Candidate Node ID:** `student/<node-id>`
- **Designated Faculty:** [faculty-systems | faculty-philosophy | faculty-law]
- **Target Branch:** `student/<node-id>/<topic>`
- **Biological Anchor ID:** `anchor-001` (or verified registered anchor)

### 2. INVARIANT SPECIFICATION AUDIT
- [ ] Conforms to `theses/SPEC_TEMPLATE.md` section structure
- [ ] Adheres to CONSTITUTION.md Lex Superior norms
- [ ] Contains no ungrounded metaphysical or semantic inflation
- [ ] File character count <= 15,000 characters

### 3. VERIFICATION TELEMETRY
Paste output of local verification commands:
```bash
python verify.py --verify-thesis theses/<THESIS_FILE>.md
python verify.py
```

### 4. VALUE ATTRIBUTION DECLARATION
* Leaf Agent Attribution: 70%
* Curriculum Root Backpropagation: 30% (decaying as 1/h^2)
