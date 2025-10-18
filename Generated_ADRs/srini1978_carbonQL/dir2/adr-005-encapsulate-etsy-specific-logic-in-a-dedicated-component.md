---
### ADR-005: Encapsulate Etsy-specific logic in a dedicated component

Status: Inferred
Context: EtsyCalculations.cs in the Controller folder and EtsyModels.cs in the Model folder indicate domain-specific logic and models centered on Etsy.
Decision: Implement Etsy-related calculations in a dedicated class/component and represent Etsy entities with dedicated models.
Consequences:
- Positive: High cohesion of Etsy-related logic; easier maintenance and extension of Etsy-specific features.
- Negative: Tight coupling to the Etsy domain in this component; reuse for non-Etsy contexts may require refactoring.