# 02_Disvalues_Diagnostics

This directory documents the ethical breakdowns, violations, and failures that counteract the 15 Canonical Values of the AI Moral Code. Disvalues are conceptualized as inverse signals or structural disruptions within AI governance, and are derived through both theoretical classification and empirical validation.

## Structure

- `AIMC_DISVALUE_MAP.csv`:  
  A record of disvalue term appearances across the validated corpus. Each row includes the `unique_id`, `disvalue_term`, the column it appeared in (`normalized_principles` or `normalized_values`), and the source text.

- `AIMC_DISVALUE_FREQUENCY_SNAPSHOT.csv`:  
  Aggregated frequency counts for each disvalue across the current corpus. This snapshot serves as the basis for risk modeling and value-disvalue link diagnostics.

## Application

These files support:
- Monitoring disvalue emergence across AI ethics documents
- Tracing how ethical harms concentrate in policy language
- Informing AI system audits and value alignment tools
- Structuring diagnostic alerts in the future Cognate Reasoning Engine

This diagnostic phase enables the AI Moral Code to recognize not only what values are present in a document—but also what **violations** are implied or embedded in its ethical structure.