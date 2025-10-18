---
### ADR-003: Backend Database Technology

**Status:** Inferred
**Context:** The application requires a database to store its data, including user information, questionnaires, responses, and analysis results. The nature of this data, potentially involving nested structures or evolving schemas (e.g., different types of questions or responses), suggests that a flexible data model could be advantageous over a rigid, relational one.
**Decision:** MongoDB, a NoSQL document database, was selected as the primary data store. This is strongly inferred from the `pymongo` library in `requirements.txt` and further supported by the presence of scripts like `excel_to_mongo_response_to_diagnosis.py`, which explicitly name the target database.
**Consequences:**
*   **Positive:**
    *   The schema-less nature of a document database provides flexibility to store complex, nested data structures (like questionnaires with various question types) easily.
    *   It's easier to evolve the data model over time without requiring complex database migrations.
    *   Horizontal scalability is often considered a strength of MongoDB, which can be beneficial as the application grows.
*   **Negative:**
    *   The lack of enforced transactions across multiple documents can make complex, multi-step operations more difficult to implement correctly compared to traditional SQL databases.
    *   Querying for complex relationships between data can be less performant or more complex than with a well-designed relational database using JOINs.