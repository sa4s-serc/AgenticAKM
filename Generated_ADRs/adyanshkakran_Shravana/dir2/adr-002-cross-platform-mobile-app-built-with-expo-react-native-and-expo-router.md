---
### ADR-002: Cross-platform mobile app built with Expo + React Native and expo-router

Status: Inferred
Context: The mobile app must target iOS, Android, and optionally web. Rapid prototyping, over-the-air updates, and minimal native build friction are desired. Files include expo-router configuration and Expo scripts.
Decision: Use Expo (SDK 50) with React Native and expo-router for file-based navigation.
Consequences:
- Positive: Faster development, OTA updates, strong ecosystem, file-based routing simplifies navigation, web support via Expo Web.
- Negative: Some native module limitations vs pure React Native CLI, potential bundle size overhead, reliance on Expo’s roadmap.