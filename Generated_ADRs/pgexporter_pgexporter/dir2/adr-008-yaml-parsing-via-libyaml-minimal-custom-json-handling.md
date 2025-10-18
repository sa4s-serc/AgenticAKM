---
### ADR-008: YAML parsing via libyaml; minimal custom JSON handling

Status: Inferred
Context: FindLibYAML.cmake and yaml_configuration.c show libyaml usage; json.c and json_configuration.c exist without an external JSON dependency.
Decision: Use libyaml for YAML parsing and implement lightweight JSON handling internally to avoid adding another external library.
Consequences:
- Positive: Keeps dependency set minimal; full control over JSON handling; consistent config pipeline.
- Negative: Maintaining custom JSON code; fewer features than mature JSON libraries unless re-implemented.