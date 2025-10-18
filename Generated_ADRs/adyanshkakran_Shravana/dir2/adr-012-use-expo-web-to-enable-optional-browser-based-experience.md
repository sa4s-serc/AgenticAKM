---
### ADR-012: Use Expo Web to enable optional browser-based experience

Status: Inferred
Context: NPM scripts include expo start --web; dependencies include react-native-web and @mui/material. Some screens/components are web-friendly.
Decision: Enable web builds of the React Native app using Expo Web and react-native-web, complemented by MUI where appropriate.
Consequences:
- Positive: Broader reach (web) with shared code; easier demos and testing without devices/emulators.
- Negative: Styling and behavior parity issues across platforms; component compatibility gaps; additional testing surface.