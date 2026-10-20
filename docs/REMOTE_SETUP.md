# PROJECT ACME: REMOTE SYNCHRONIZATION SPECIFICATION
> **Protocol RFC-001 | Operational Guide**

---

### 1. REMOTE ENVIRONMENT STATUS
During the Genesis Phase 3 probe:
- **Configured Remotes:** `None`
- **GitHub CLI (`gh`):** Not installed or not on system `PATH`
- **Current Canonical Branch:** `main`
- **Current Release Tag:** `v1.0.0`
- **Air-Gapped Backup:** `acme-v1.0.0.bundle` (contains full Git history, `main`, and `v1.0.0`)

---

### 2. CONNECTING TO A REMOTE GITHUB REPOSITORY

#### Step 2.1: Create Remote Repository on GitHub
Create a new, empty GitHub repository (do **not** initialize with README, .gitignore, or license):
- Name: `acme` (or `acme-academy`)
- Visibility: Public or Private

#### Step 2.2: Link Remote Origin
Run from repository root:
```bash
# Using SSH (Recommended)
git remote add origin git@github.com:<YOUR_ORGANIZATION_OR_USER>/acme.git

# Or using HTTPS
git remote add origin https://github.com/<YOUR_ORGANIZATION_OR_USER>/acme.git
```

#### Step 2.3: Push Canonical Branches & Cryptographic Tags
```bash
git push -u origin main
git push origin --tags
```

---

### 3. AIR-GAPPED DEPLOYMENT & RESTORATION

If network isolation is required or GitHub remote is unavailable, the entire verified Merkle tree can be replicated instantly from the verified bundle:

```bash
# Verify bundle integrity
git bundle verify acme-v1.0.0.bundle

# Replicate complete repository
git clone acme-v1.0.0.bundle acme-replica

# Verify cloned replica
cd acme-replica
git log --graph --oneline
python verify.py --verify-all
python verify.py --audit-ledger
```
