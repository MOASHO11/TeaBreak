# TeaBreak | اشرب شاي ☕ — Cryptographic Release Manifest
**Version:** `2.1.0` (Public Release)  
**Release Tag:** `v2.1.0`  
**Official Repository:** `https://github.com/moasho11/TeaBreak`  
**Author Signature:** `#MOASHO11𓂀` ([LinkedIn Profile](https://www.linkedin.com/in/moasho11/))  
**Generated At:** 2026-11-17 01:03:55 UTC

---

## 🔒 Cryptographic File Integrity & SHA-256 Checksums

Every file in this release package has been audited, verified, and signed with SHA-256 digests. You can verify the integrity of any file prior to installation using standard operating system utilities.

| File | Size (Bytes) | SHA-256 Checksum |
|---|:---:|---|
| `notify_on_stop.py` | `61,365` | `82f83adfdbcaef046528eb1196cc3c57cd27871c3661410543bd70f07a62e17f` |
| `MASTER_WIZARD.md` | `70,893` | `a19cd86993b68e6276575075e54308163563f1bc978bdeadc27ea38684ddf641` |
| `README.md` | `9,653` | `de1ca5946e4f66168ed42cb3ee4f5d6a3761a93d95ddac58723b82a512a12770` |
| `README.ar.md` | `13,228` | `b39d445ea33d7ea63b761a5d8b429ff008365fd6118ce91bef574b773da2cdbb` |
| `tests/test_regression.py` | `35,851` | `03754153ee6e434ca8b97e56eb0d30524f9c135bf7bdac637b442ae379f4cebc` |

---

## 🛡️ Parity Verification Protocol

The executable Python script embedded inside `MASTER_WIZARD.md` is guaranteed to be a **100% byte-for-byte identical copy** of `notify_on_stop.py`.

### How to verify on Windows (PowerShell):
```powershell
Get-FileHash -Algorithm SHA256 .\notify_on_stop.py
Get-FileHash -Algorithm SHA256 .\MASTER_WIZARD.md
```

### How to verify on Linux / macOS:
```bash
sha256sum notify_on_stop.py
sha256sum MASTER_WIZARD.md
```

---

## 🔍 Security & Privacy Audit Certification

- [x] **Zero OS Control Policy:** Strictly confirmed. Zero execution of OS-level administrative commands.
- [x] **Zero Third-Party Dependencies:** 100% Python 3 standard library. Zero external packages required.
- [x] **Zero Telemetry:** No user data, analytics, tokens, prompt text, or workspace paths are collected or leaked.
- [x] **Fail-Closed Git Ignore Verification:** Confirmed active. Prevents saving private ntfy topics if `.gitignore` rules fail.
- [x] **Deduplication Engine:** Verified. Automatically cleans and deduplicates hook registrations across current and legacy keys.
- [x] **Dual Scope Support:** Both Workspace Hook and Global Plugin modes verified without conflicts.

---
**Verified and Released by #MOASHO11𓂀**  
*خلّي مساعدك يشتغل، واشرب شايك ☕*
