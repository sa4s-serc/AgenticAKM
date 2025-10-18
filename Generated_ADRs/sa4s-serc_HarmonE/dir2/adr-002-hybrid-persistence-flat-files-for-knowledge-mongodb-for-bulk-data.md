---
### ADR-002: Hybrid persistence: flat files for knowledge, MongoDB for bulk data

Status: Inferred
Context: The presence of knowledge/*.csv and *.json files (e.g., drift.csv, mape_log.csv, thresholds.json) suggests file-based storage for operational knowledge. The requirements include pymongo and tools like tools/store_pems.py, implying MongoDB is used to ingest/store larger datasets (e.g., PEMS) and possibly models.
Decision: Use CSV/JSON files under knowledge/ for the MAPE-K knowledge base and logs; use MongoDB for larger, operational datasets and potentially model artifacts.
Consequences:
- Positive: Human-readable, versionable knowledge; simple local workflows; scalable storage for large datasets via MongoDB.
- Negative: Increased operational complexity managing two storage mechanisms; file-based storage has limited concurrency and can be brittle without locking; syncing state between file store and DB must be managed.