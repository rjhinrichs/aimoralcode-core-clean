# ver_meme_02_local_bib_exact_match

## Classification
- Type: verification meme
- Status: experimental, additive
- Cognitive Role: internal verification through human-led local file matching
- Purpose: confirms alignment between MASTER entry and previously downloaded file
- Naming Convention: lower case for evolving logic capsule

## Trigger Condition
- MASTER row has no valid URL (e.g., contains local placeholder: ../../...)
- PDF or DOC is already located in /book/BIBLIOGRAPHY
- Title, issuer, and year can be matched directly from file contents

## Actions
1. Open the document in Bibliography folder.
2. Verify alignment with MASTER values:
   - `name_of_document`
   - `issuer`
   - `date_of_issue`
3. Rename file using snake_case title convention.
4. Update MASTER:
   - `matched_pdf`: [snake_case_filename]
   - `confirmed_match`: Yes
   - `citation_label`: Issuer, Year
   - `citation_source`: Full title as it appears on document

## Use Case Anchor
- DOC_ID: doc_131
- Example: "Human Rights and artificial intelligence (CDDH-IA)", Council of Europe, 2024

## Notes
This pattern emphasizes fidelity of source validation via internal file logic. Designed for cases where local files were archived early and need forensic re-alignment to current database schema.