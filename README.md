## Why This Project

- **Problem**: Initial analysis suggeset that there is a helpful additional explanatory note in NACE v2.1 for classifying a case not available in ISIC rev5. No official correspondence exists between the latest ISIC v5 and NACE v2.1, yet analysis need cross-system comparability.
- **Approach**: Use LLM-assisted semantic mapping, then validate against master code lists to ensure 4-digit coverage and consistency.
- **Outcome**: A mapping in JSON and Excel with confidence and match-type metadata.

## Data Inputs

- ISIC master: ISIC rev5 excel from [UNStats](https://unstats.un.org/unsd/classifications/Econ)
- NACE master: NACE v2.1 excel from [EU ShowVoc](https://showvoc.op.europa.eu/#/datasets/ESTAT_Statistical_Classification_of_Economic_Activities_in_the_European_Community_Rev._2.1._%28NACE_2.1%29/downloads)

## Example Output


original output is located `/raw-output`, while the combined and validation in `/processed-output`
```
...
{
  "isic_codes": ["0111"],
  "nace_codes": ["01.11"],
  "confidence": "High",
  "match_type": "one-to-one"
}
{
  "isic_codes": ["0141"],
  "nace_codes": ["01.41", "01.42"],
  "confidence": "High",
  "match_type": "one-to-many"
}
...
```

## Some Findings
