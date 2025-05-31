# ver_meme_05_internal_filename_match_from_alpha_sort

## Classification
- Type: verification meme
- Status: confirmed, retrievable
- Cognitive Role: filename-driven confirmation logic
- Purpose: resolves document validation using internal BIBLIOGRAPHY sort and metadata alignment
- Naming Convention: lowercase to reflect adaptive and inference-based confirmation method

## Trigger Condition
- MASTER row contains ambiguous or malformed `matched_pdf` or URL
- Internal BIBLIOGRAPHY folder contains a PDF with matching title
- File is confirmed through alpha sorting and content alignment

## Actions
1. Sort the `/book/BIBLIOGRAPHY` directory alphabetically.
2. Visually locate filename that closely matches `name_of_document`.
3. Open file to confirm it matches `issuer`, `title`, and `date_of_issue`.
4. Rename the file using strict snake_case convention.
5. Update MASTER:
   - `matched_pdf`: renamed file
   - `confirmed_match`: Yes
   - `citation_label`: Issuer, Year
   - `citation_source`: Document Title
   - `URL`: Link to a direct PDF version of the source, if superior

## Use Case Anchor
- DOC_ID: doc_005
- Title: A Next Generation Artificial Intelligence Development Plan
- Issuer: State Council of China
- URL: https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2021-03-02%20China%27s%20New%20Generation%20Artificial%20Intelligence%20Development%20Plan-%202017.pdf
- matched_pdf: a_next_generation_artificial_intelligence_development_plan.pdf

## Notes
This method validates file presence and content using internal evidence, human sorting, and URL optimization. This verification strategy is useful when URL metadata is unreliable or incomplete.