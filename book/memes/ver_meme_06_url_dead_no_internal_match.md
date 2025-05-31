# ver_meme_06_url_dead_no_internal_match

## Classification
- Type: verification meme
- Status: unresolved
- Cognitive Role: identifies breakdowns in external reference availability
- Purpose: captures cases where a listed URL no longer resolves, and no file exists locally
- Naming Convention: lowercase reflects exploratory, diagnostic state

## Trigger Condition
- `confirmed_match` is set to Yes in the MASTER, but:
  - The linked URL returns a 404 or dead redirect
  - The `matched_pdf` file is not found in the BIBLIOGRAPHY directory
  - No cached version or internal backup is available

## Actions
1. Manually verify that the URL returns a 404 or similar access failure.
2. Search local BIBLIOGRAPHY for `matched_pdf` entry (if any).
3. If both fail:
   - Set `confirmed_match` to `No`
   - Clear `matched_pdf` field or add comment `Missing PDF`
   - Add a `note` field: `URL dead, PDF not found`
4. Attempt recovery by:
   - Searching public repositories, author pages, or archives
   - Using the Wayback Machine for URL snapshots
   - Reaching out to the issuing body or authors
5. Reclassify upon successful document retrieval.

## Use Case Anchor
- DOC_ID: doc_001
- Title: 10 Principles of Responsible AI
- Issuer: Women Leading in AI
- URL: https://www.womenleadinginai.org/10-principles (404 as of 2025)

## Notes
This meme captures ethical and archival fragility. A key reminder that data fidelity is temporal, and responsible repositories must build resilience into their access logic. Verification requires both external traceability and local redundancy.