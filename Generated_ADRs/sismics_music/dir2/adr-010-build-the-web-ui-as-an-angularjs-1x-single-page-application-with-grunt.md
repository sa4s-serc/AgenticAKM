---
### ADR-010: Build the web UI as an AngularJS 1.x single-page application with Grunt

Status: Inferred
Context: music-web includes an AngularJS 1.x app (controllers, directives, services), built with Grunt tasks (concat, uglify, less, etc.), and vendored libraries under src/lib.
Decision: Implement the web frontend as a SPA using AngularJS 1.x and build assets with Grunt.
Consequences:
- Positive: Rapid development for the timeframe; cohesive client-side routing and state; straightforward REST integration.
- Negative: Aging stack (maintenance, security updates); manual asset management; harder long-term modernization compared to newer frameworks and build tools.