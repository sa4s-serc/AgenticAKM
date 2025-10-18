---
### ADR-004: MongoDB with Mongoose for Data Persistence

**Status:** Inferred

**Context:** The application requires a database to store and manage data for users, food items, orders, and shopping carts. The data model may evolve, so a flexible schema is advantageous. An effective way to interact with the database from Node.js was also necessary.

**Decision:** MongoDB was chosen as the database, with Mongoose serving as the Object Data Modeling (ODM) library. The presence of `mongoose` in `backend/package.json` and model files like `foodModel.js` and `userModel.js` confirms this. The file `mongodbatlaspass.txt` strongly implies that a managed cloud service, MongoDB Atlas, is being used for hosting.

**Consequences:**
*   **Positive:**
    *   MongoDB's document-oriented structure maps well to JavaScript objects, making it intuitive to work with in a Node.js environment.
    *   Mongoose provides schema definition, data validation, and business logic hooks, bringing a level of structure and predictability to the data layer.
    *   Using a managed service like MongoDB Atlas abstracts away the complexities of database administration, scaling, and backups.
*   **Negative:**
    *   NoSQL databases like MongoDB lack the native support for complex joins and transactions found in traditional SQL databases.
    *   Mongoose adds an abstraction layer that can, if not used carefully, obscure the performance of underlying database operations.