---
### ADR-011: ReactMarkdown with raw HTML enabled

Status: Inferred
Context: Frontend depends on react-markdown, rehype-raw, rehype-highlight, remark-gfm; components likely render LLM content.
Decision: Render markdown responses using ReactMarkdown with plugins for GFM, syntax highlighting, and raw HTML support.
Consequences:
- Positive: Rich, flexible rendering of AI content and code blocks.
- Negative: Enabling raw HTML introduces XSS risk; sanitization and content trust boundaries must be managed carefully.