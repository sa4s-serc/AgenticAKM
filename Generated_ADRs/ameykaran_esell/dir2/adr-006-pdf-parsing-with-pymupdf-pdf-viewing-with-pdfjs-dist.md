---
### ADR-006: PDF parsing with PyMuPDF; PDF viewing with pdfjs-dist

Status: Inferred
Context: PyMuPDF listed; modules like extract_paper_images.py and process_pdf.py exist; frontend depends on pdfjs-dist and has PDF viewer components.
Decision: Use PyMuPDF to analyze/extract PDF content on the backend; render PDFs in the browser with pdfjs-dist.
Consequences:
- Positive: Robust parsing and image extraction; consistent in-browser rendering.
- Negative: PyMuPDF adds native dependencies; PDF parsing can be resource-intensive and require tuning.