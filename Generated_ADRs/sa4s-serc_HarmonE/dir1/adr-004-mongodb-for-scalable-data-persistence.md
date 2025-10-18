---
### ADR-004: MongoDB for Scalable Data Persistence

**Status:** Inferred
**Context:** While the core MAPE-K loop uses a simple file-based knowledge base, the system likely handles larger volumes of data, such as raw time-series data for training (`tools/store_pems.py`), historical prediction logs, or extensive model evaluation results. A more robust and scalable persistence solution was needed for these purposes, one that could be queried efficiently.
**Decision:** MongoDB was chosen as the database for scalable data storage. The inclusion of the `pymongo` driver in `requirements.txt` is the key indicator for this decision. It likely serves as the primary datastore for raw data ingested into the system and for long-term archival of results and logs.
**Consequences:**
*   **Positive:** MongoDB's document-based model provides schema flexibility, which is advantageous for storing complex, nested data structures or evolving data formats. It is designed to scale horizontally, making it suitable for handling large datasets.
*   **Negative:** This introduces an external service dependency. The MongoDB server must be installed, configured, and maintained separately from the application. This adds operational complexity compared to an embedded or file-based-only solution.