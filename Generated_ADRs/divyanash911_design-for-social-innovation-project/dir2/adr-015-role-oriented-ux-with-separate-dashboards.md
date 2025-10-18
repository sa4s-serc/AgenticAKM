---
### ADR-015: Role-oriented UX with separate dashboards

Status: Inferred
Context: Components exist for ParentDashboard, TeacherDashboard, PsychologistDashboard, and ChildDashboard; ProfileSection and ViewResponse components suggest role-specific data.
Decision: Provide distinct UI flows and pages for different user roles.
Consequences:
- Positive: Tailored experiences improve clarity and security by limiting surface area per role.
- Negative: Increases UX complexity and testing scope; requires backend enforcement of authorization to complement UI-level segregation.