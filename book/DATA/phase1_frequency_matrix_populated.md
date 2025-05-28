# Phase 1 Frequency Matrix

This file contains the **populated** value frequency counts for the first phase of the AI Moral Code analysis across 291 ethical AI documents. Each row corresponds to a document, with binary indicators for the presence (1) or absence (0) of a specific ethical value or principle.

## File: `phase1_frequency_matrix_populated.csv`

### Structure

- **Unique_ID**: Document identifier (e.g., `DOC_001`)
- **Canonical Values**: Columns for each value (e.g., `Justice`, `Transparency`, `Responsibility`, etc.) now populated based on text matching from original term fields.
- **Metadata Fields**:
  - `Name of Document/Website`
  - `Issuer`
  - `Sector`
  - `Country of Issuer`
  - `URL` (if available)

### Purpose

This matrix serves as a foundational dataset for:
- Quantitative validation of Phase 1 findings
- Source traceability for simulation and use-case development
- Mapping canonical values to global governance documentation
- Visualization of ethical value distributions across international sources

### Source Files

- Metadata: `MASTER AI Moral Code Taxonomy with Weights May 2025.xlsx`
- Term Extraction: `291 Docs` tab
- Value Counts: `AI_Moral_Code_Phase_1_Frequency_Matrix.xlsx`

This file is the **canonical, verifiable source** for all Phase 1 frequency-based claims, simulations, and analytical outputs.

_Last updated: May 2025_