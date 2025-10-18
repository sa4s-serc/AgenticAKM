---
### ADR-005: Automation of Development and Release Tasks using Ruby-based Tooling

**Status:** Inferred

**Context:** Maintaining a high-quality open-source library involves many repetitive tasks beyond writing code, such as running tests, linting code, managing changelogs, updating version numbers, and publishing to package managers. Manually performing these tasks is time-consuming and prone to human error.

**Decision:** The project automates its build, test, and release pipeline using a suite of Ruby-based tools. The `Gemfile` specifies dependencies like `rake` (for task automation), `cocoapods` (for linting the podspec), `octokit` (for GitHub API interactions), and `xcpretty` (for formatting build output). The `Rakefile` and the `scripts/` directory contain the automation logic for tasks like bootstrapping, updating changelogs (`update_changelog.sh`), and updating package specifications (`update_podspec.sh`). This entire process is orchestrated in CI via `.circleci/config.yml`.

**Consequences:**
*   **Positive:**
    *   **Consistency and Reliability:** Automation ensures that tasks are performed in the same way every time, reducing errors and ensuring consistency across releases.
    *   **Increased Efficiency:** Maintainers can focus on development rather than on manual, repetitive administrative tasks.
    *   **Improved Contributor Experience:** Scripts like `bootstrap.sh` simplify the process for new contributors to set up the development environment.
*   **Negative:**
    *   **Technology Stack Proliferation:** The project requires developers and maintainers to have a working Ruby environment in addition to the standard Swift/Xcode toolchain.
    *   **Maintenance of Tooling:** The automation scripts and their Ruby dependencies must be maintained over time, which adds another layer of work.