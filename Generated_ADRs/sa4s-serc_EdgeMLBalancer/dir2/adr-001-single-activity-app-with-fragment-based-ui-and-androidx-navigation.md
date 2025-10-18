### ADR-001: Single-Activity app with Fragment-based UI and AndroidX Navigation

Status: Inferred
Context: The codebase contains MainActivity plus multiple Fragments (HomeFragment, PermissionsFragment, CameraFragment) and a navigation graph (res/navigation/nav_graph.xml). Generated navigation classes (CameraFragmentDirections, HomeFragmentDirections, PermissionsFragmentDirections) and the Safe Args Gradle plugin are present.
Decision: Adopt a single-activity architecture with screen flows implemented as Fragments, orchestrated by AndroidX Navigation with Safe Args.
Consequences: 
- Positive: Clear navigation graph, back-stack handling, and type-safe argument passing; easier state and lifecycle management.
- Negative: Fragment-based complexity (lifecycle, view lifecycles); learning curve for Navigation Component.