---
### ADR-009: Hash passwords with bcrypt-family libraries

Status: Inferred
Context: Dependencies include bcrypt and bcryptjs (and a misspelled bcrpyt), indicating password hashing choices and potential cross-platform fallback.
Decision: Use bcrypt-based hashing for user credentials, with capability to switch to bcryptjs where native builds are problematic.
Consequences:
- Positive: Industry-standard hashing; compatibility across environments via js fallback.
- Negative: Native bcrypt build issues on some platforms; bcryptjs has lower performance/security characteristics than native bcrypt.