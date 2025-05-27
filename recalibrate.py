import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

import pandas as pd
from nltk.stem import WordNetLemmatizer
from fuzzywuzzy import process
import nltk

# Ensure NLTK datasets are available
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load your term frequency file (update path as needed)
terms_df = pd.read_csv("Categorized_Ethical_Terms_Expanded.csv")

# Load your taxonomy Excel
taxonomy_df = pd.read_excel("MASTER AI Moral Code Taxonomy with Weights April  2025.xlsx", sheet_name="Value Categories")
value_map = taxonomy_df[['Value', 'Values Category']].dropna()
value_map.columns = ['Ethical Term', 'Recalibrated Category']

# Normalize terms using lemmatizer
lemmatizer = WordNetLemmatizer()
def normalize(term):
    words = term.lower().split()
    return " ".join([lemmatizer.lemmatize(w) for w in words])

taxonomy_terms = value_map["Ethical Term"].unique().tolist()
taxonomy_terms_normalized = [normalize(t) for t in taxonomy_terms]

# Fuzzy match each term
def fuzzy_map(term):
    norm_term = normalize(term)
    match, score = process.extractOne(norm_term, taxonomy_terms_normalized)
    if score >= 85:
        return taxonomy_terms[taxonomy_terms_normalized.index(match)]
    return None

# Apply fuzzy matching to terms
terms_df["Fuzzy Matched Term"] = terms_df["Ethical Term"].apply(fuzzy_map)

# Merge recalibrated categories from fuzzy matches
final_df = pd.merge(
    terms_df,
    value_map.rename(columns={"Ethical Term": "Fuzzy Matched Term"}),
    on="Fuzzy Matched Term",
    how="left"
)

# Assign final category
final_df["Final Category"] = final_df["Recalibrated Category"].combine_first(terms_df["Category"])

# Save output
final_df.to_csv("Fully_Recalibrated_Ethical_Terms.csv", index=False)
print("Classification complete. Output saved as Fully_Recalibrated_Ethical_Terms.csv.")

