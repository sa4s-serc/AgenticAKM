### ADR-001: Adopt SAML-based model-driven development for system specification

Status: Inferred
Context: The repository contains multiple .capssaml models and a metamodel (metamodel-saml.puml), alongside parsers and generators that work from SAML inputs. There is also an Eclipse workspace with SAML samples, indicating the modeling workflow originates in a graphical/modeling tool.
Decision: Use CAPS SAML as the primary source of truth for system specifications and drive code generation from these models.
Consequences: 
- Positive: Consistent, model-first development; traceability from models to code; clearer separation between design and implementation.
- Negative: Dependency on specific modeling tools (Eclipse-based); learning curve for SAML; need to maintain parsers aligned with model evolution.