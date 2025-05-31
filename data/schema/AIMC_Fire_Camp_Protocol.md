
## AIMC Fire Camp Protocol

### Purpose
To document key interventions, pause points, and conflict resolution protocols that prevent global data corruption or ethical misclassification in the MASTER AI Moral Code database.

---

### Merge Camp: Duplicate Records – Same Document

**Date**: May 29, 2025  
**Action**: Merge of DOC_023 into DOC_251

**Primary Record**:  
- **DOC_251**  
- Name of Document: *AI Principles of Telefónica Spain 2018*  
- URL: https://www.telefonica.com/wp-content/uploads/sites/7/2021/11/principios-ai-eng-2018.pdf  
- `matched_pdf`: `ai_principles_of_telefonica_spain_2018.pdf`  
- `confirmed_match`: `Yes`

**Secondary Record**:  
- **DOC_023**  
- Action Taken:  
  - Notes: `Duplicate of DOC_251 – Merge completed`
  - `matched_pdf`: `Merged with DOC_251`
  - `confirmed_match`: `Merged`

**Justification**:  
Content, issuer, and year align. URL is verified and matches PDF. Keeping DOC_251 strengthens traceability; DOC_023 archived for version control.

---

### Retirement Protocol – Soft Deletion Guidelines

To maintain referential and historical integrity, records should not be deleted or renumbered. Instead, adopt the following soft deletion standard:

- Keep `Unique_ID` static (e.g., `DOC_023`)
- Set `record_status`: `retired`
- Add note explaining the action, e.g., `Retired – Merged into DOC_251`
- Set `matched_pdf`: `Merged`
- Set `confirmed_match`: `Merged`

This ensures schema stability, prevents downstream analytic error, and supports archival validation in scholarly and machine-readable forms.
