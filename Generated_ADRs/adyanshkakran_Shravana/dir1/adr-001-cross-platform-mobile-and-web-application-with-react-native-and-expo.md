### ADR-001: Cross-Platform Mobile and Web Application with React Native and Expo

**Status:** Inferred
**Context:** The project required a user-facing application that could run on iOS, Android, and the Web. Building and maintaining separate native codebases for each platform would be time-consuming and expensive, requiring specialized teams for each technology stack. A solution was needed to maximize code reuse and accelerate development.
**Decision:** The frontend application, `shravana-app`, was built using React Native with the Expo framework. This is evidenced by the `package.json` file, which lists `react-native`, `expo`, `expo-router`, and `react-native-web` as dependencies, along with TypeScript (`.tsx` files) for type safety.
**Consequences:**
*   **Positive:**
    *   **Code Reusability:** A single JavaScript/TypeScript codebase can be deployed to iOS, Android, and the web, significantly reducing development and maintenance effort.
    *   **Faster Development:** The Expo ecosystem provides pre-built components, simplifies the build and deployment process, and offers tools like "over-the-air" updates.
    *   **Single Team:** A team of developers skilled in React and JavaScript can build and maintain the application across all target platforms.
*   **Negative:**
    *   **Abstraction Layer:** While powerful, Expo can sometimes limit direct access to certain low-level native device APIs, although this is becoming less of an issue.
    *   **Performance:** For extremely graphics-intensive or computationally heavy applications, React Native might not match the performance of a fully native application.