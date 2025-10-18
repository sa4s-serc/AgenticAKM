---
### ADR-009: Data ingestion from Excel into MongoDB for rules and mappings

Status: Inferred
Context: Scripts excel_to_mongo_response_to_diagnosis.py and excel_to_mongo_diagnosis_to_summary.py indicate rule tables maintained in spreadsheets.
Decision: Maintain mappings/rules in Excel and provide scripts to import them into MongoDB.
Consequences:
- Positive: Non-developers can edit rule data; rapid iteration on rules without code changes.
- Negative: Risk of data drift and versioning issues; requires controlled import processes and validation.