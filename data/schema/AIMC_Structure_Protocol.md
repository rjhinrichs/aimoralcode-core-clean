
# AIMC Structure Protocol

## Purpose
To ensure the AI Moral Code (AIMC) database structure is continuously refined for:
- Semantic fidelity
- Computational efficiency
- Interpretability
- Grace and elegance in architecture

## Principles

### 1. Field Integrity
- Every field must serve a human or machine purpose.
- Human-readable fields (e.g., `Name of Document`) preserve sentence case and original intent.
- Machine-actionable fields (e.g., `matched_pdf`, `canonical_snake_title`) use strict formatting (snake_case).

### 2. Value Curation
- Canonical forms represent normative identities (e.g., `think20_japan_2019.pdf`).
- Compress only when meaning is preserved.
- Track legacy labels in the `Notes` or `original_filename` columns for transparency.

### 3. Naming Conventions
- `Name of Document`: sentence case, original title
- `matched_pdf`: snake_case, max 8-10 words, includes file extension
- `confirmed_match`: Yes/No flag, based on human-verified content inspection
- `citation_label`: APA 7 style
- `canonical_snake_title`: optional compressed field for graph-based processing

### 4. Graceful Execution
- Frictionless transformation between formats (CSV → JSON → PDF)
- Intelligent ordering of fields (from bibliographic to ethical analysis)
- No redundancy unless required for linkage

### 5. Elegant Architecture
- All folders reflect structural intent:
  - `/data/schema/`: metadata blueprints
  - `/data/verified/`: truth-validated document links
  - `/exports/`: downstream outputs for ML, publishing, and governance engines
- Markdown documentation serves as the ethical memory of the dataset

---

## Operational Mandate

This protocol applies to:
- Schema expansions
- Data ingestion logic
- Renaming functions
- Inference models
- Future publication pipelines

Grace and elegance are not abstract. They are encoded.
