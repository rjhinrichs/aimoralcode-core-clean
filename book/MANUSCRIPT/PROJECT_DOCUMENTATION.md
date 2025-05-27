# Project Documentation and Directory Map

This document maps the structure and logic of the AI Moral Code repository, including file roles, folder usage, and contributor protocol. It is your single point of reference for locating all components of the project.

---

## Core Structure

### /00_Foundations/
- Ethical theories, philosophical grounding, and justification logic

### /01_Canonical_Values/
- [DEPRECATED] Merged into /AI_Moral_Code/
- Use AI_Moral_Code for all value-related content going forward

### /02_Disvalues_Diagnostics/
- Definitions and operational logic of disvalues
- Structured .csv and .json for tool integration

### /03_Conflict_Mapping/
- Logical and conceptual conflict zones
- Moral tensions and adversarial casework

### /04_Implementation/
- AIBQ scoring models
- Ethics-in-practice simulations
- ML-compatible scoring logic

### /05_Web_Architecture/
- Glossary JSON export
- GitHub Pages metadata and render logic

### /AI_Moral_Code/
- Canonical values
- Glossary inputs
- Disvalue and value weight models

### /AI_Moral_Code_Book/
- /DATA/: Analysis files cited in the manuscript
- /MANUSCRIPT/: Draft chapters
- /ARCHIVE/: Older or pre-versioned drafts
- /PRESENTATIONS/: Conference slide decks
- /SOURCES/: PDFs, articles, and citations

### /exports/
- Public-ready JSONs, PDFs, and presentation decks

---

## Workflow Summary

1. **Local Work Directory**:  
   `C:\Users\Ran\OneDrive\Desktop\Documents\GitHub\aimoralcode-core`

2. **Working Style**:
   - All edits done locally (e.g., .md, .json, .csv)
   - Changes reviewed via GitHub Desktop
   - Commits made with summaries
   - Push to origin daily or after major task

3. **Secondary Interfaces**:
   - GitHub Web for quick markdown changes
   - Ubuntu CLI for advanced Git commands or Git LFS control

---

## External Resources

- Cognates UI: `cognates-browser/`
- Web staging: `aimoral-jekyll/`
- Linked glossary files exported via `data/` → `exports/`

---

## Notes
- For any new contributors, read this file and the Master Plan first
- All folders will have README.md files explaining their use
