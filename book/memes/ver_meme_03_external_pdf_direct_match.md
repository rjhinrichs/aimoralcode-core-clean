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
   - `country`
3. Rename using snake_case based on document title.
4. Save into /book/BIBLIOGRAPHY.
5. Update MASTER:
   - `matched_pdf`: [snake_case].pdf
   - `confirmed_match`: Yes
   - `citation_label`: Issuer, Year
   - `citation_source`: Title of Document

## Use Case Anchors
- DOC_003  
  Title: 5 Trends for 2025  
  Issuer: IBM Institute for Business Value (IBM IBV)  
  Country: USA  
  matched_pdf: 5-trends-for-2025-report.pdf  
  confirmed_match: Yes

- DOC_006  
  Title: Adobe's AI Ethics Principles  
  Issuer: Adobe Inc.  
  Country: USA  
  matched_pdf: adobe_ai_ethics_principles.pdf  
  confirmed_match: Yes

- DOC_007  
  Title: AI and Islamic Ethics: A Framework for Ethical AI Development Based on Maqasid Al-Shariah  
  Issuer: ICANEAT  
  Country: Indonesia  
  matched_pdf: artificial_intelligence_islamic_ethics_maqasid_al_shariah.pdf  
  confirmed_match: Yes

## Notes
This is the preferred verification method when high-quality, publisher-hosted PDFs are available. This meme requires minimal intervention and should be prioritized when possible.