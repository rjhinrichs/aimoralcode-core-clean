# ver_meme_03_external_pdf_direct_match

## Classification
- Type: verification meme
- Status: stable, reliable
- Cognitive Role: external file validation via live URL
- Naming Convention: lower case reflects additive, modular logic unit

## Trigger Condition
- MASTER row includes a live URL pointing directly to a PDF
- File is downloaded and stored in /book/BIBLIOGRAPHY
- All identifying fields align (title, issuer, year)

## Actions
1. Follow the external URL and confirm a working PDF download.
2. Open the file to ensure metadata matches:
   - `name_of_document`
   - `issuer`
   - `date_of_issue`
3. Rename using snake_case based on document title.
4. Save into /book/BIBLIOGRAPHY.
5. Update MASTER:
   - `matched_pdf`: [snake_case].pdf
   - `confirmed_match`: Yes
   - `citation_label`: Issuer, Year
   - `citation_source`: Title of Document

## Use Case Anchor
- DOC_ID: doc_003
- Title: "5 Trends for 2025"
- Issuer: IBM Institute for Business Value (IBM IBV)
- Year: 2025
- URL: https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/business-trends-2025
- matched_pdf: `5-trends-for-2025-report.pdf`

## Notes
This is the preferred verification method when high-quality, publisher-hosted PDFs are available. This meme requires minimal intervention and should be prioritized when possible.