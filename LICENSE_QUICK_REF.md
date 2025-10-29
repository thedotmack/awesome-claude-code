# License Compliance - Quick Reference

## TL;DR

**Problem:** Upstream uses CC BY-NC-ND 4.0 which prohibits derivative works. Our fork violates this.

**Status:** Compliance issue identified, resolution in progress.

**Next Steps:** Contact upstream for relicensing, explore alternatives if declined.

**Timeline:** 2-4 weeks for resolution.

---

## What's Wrong?

| Item | Current Status | Issue |
|------|----------------|-------|
| **Upstream License** | CC BY-NC-ND 4.0 | "ND" = No Derivatives allowed |
| **This Fork** | Modified version | Violates NoDerivatives clause |
| **Our LICENSE file** | CC BY-NC-ND 4.0 | Correct (inherited) |
| **FORK_README.md** | ~~"MIT License"~~ | ❌ Was incorrect, now fixed |
| **pyproject.toml** | ~~"MIT License"~~ | ❌ Was incorrect, now fixed |

## What It Means

### Can Do (under CC BY-NC-ND 4.0):
✅ View and read the code  
✅ Fork privately on GitHub (per GitHub TOS)  
✅ Make private modifications for personal use  
✅ Share exact copies (with attribution, non-commercial)

### Cannot Do:
❌ **Distribute modified versions publicly** (This fork violates this)  
❌ Use commercially  
❌ Create and share derivative works  
❌ Adapt or transform and redistribute

## Resolution Options

### 1. Request Upstream Relicensing (PRIORITY)
**Action:** Ask upstream to change to MIT/Apache 2.0  
**If successful:** Continue current approach with proper license  
**Probability:** Unknown, worth trying  
**Effort:** Low (just ask)

### 2. Rebuild from Scratch
**Action:** Create entirely original content  
**If needed:** Can't copy any upstream content  
**Probability:** 100% success  
**Effort:** Very high

### 3. Complement, Don't Fork
**Action:** Link to upstream, add supplementary content  
**If needed:** Change from "fork" to "companion"  
**Probability:** 100% success  
**Effort:** Medium

### 4. Limited Fair Use
**Action:** Database of facts with original commentary  
**If needed:** Minimal creative expression  
**Probability:** 60-70% success  
**Effort:** Medium-high, legal risk

## Action Items Completed

- [x] Identified and documented the issue
- [x] Created LICENSE_COMPLIANCE.md (comprehensive analysis)
- [x] Created NOTICE.md (public status notice)
- [x] Updated README.md (added compliance warning)
- [x] Fixed FORK_README.md (removed incorrect MIT claim)
- [x] Fixed pyproject.toml (removed incorrect license classifier)
- [x] Created UPSTREAM_CONTACT_TEMPLATE.md (message template)
- [x] Created this quick reference guide

## Action Items Pending

- [ ] Contact upstream maintainer (use UPSTREAM_CONTACT_TEMPLATE.md)
- [ ] Add notice to issue templates
- [ ] Pause new submissions (add note to submission form)
- [ ] Update CONTRIBUTING.md with licensing notice
- [ ] Monitor for upstream response (2-4 week window)
- [ ] Execute chosen resolution path based on response

## Documents

- **[LICENSE_COMPLIANCE.md](./LICENSE_COMPLIANCE.md)** - Full analysis (10K+ words)
- **[NOTICE.md](./NOTICE.md)** - Public notice (brief)
- **[UPSTREAM_CONTACT_TEMPLATE.md](./UPSTREAM_CONTACT_TEMPLATE.md)** - Message template
- **This file** - Quick reference

## Key Dates

- **2025-10-29**: Issue identified and documented
- **2025-10-29**: Documentation created and published
- **Target: 2025-11-01**: Contact upstream maintainer
- **Target: 2025-11-15**: Resolution deadline
- **Target: 2025-11-30**: Full compliance achieved

## Recommended License (When We Can Choose)

**MIT License** is recommended because:
- Extremely simple and clear
- Maximum community adoption
- Allows derivatives and modifications
- Permits commercial and non-commercial use
- Only requires attribution
- Standard for awesome-lists

Alternative: **Apache 2.0** (if patent protection needed)

## Questions?

See [LICENSE_COMPLIANCE.md](./LICENSE_COMPLIANCE.md) for detailed information, or open an issue.

---

**Status:** Active issue, resolution in progress  
**Last Updated:** 2025-10-29  
**Next Review:** Upon upstream response or 2025-11-15
