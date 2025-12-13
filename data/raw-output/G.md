Based on my analysis of the provided ISIC and NACE codes for Section G (Wholesale and Retail Trade), here is the correspondence mapping. The structure is highly similar, with NACE providing more granular detail, especially in the wholesale agent activities (46.1) and retail intermediation (47.9).

```json
{
  "mappings": [
    {
      "isic_codes": ["G"],
      "nace_codes": ["G"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["46"],
      "nace_codes": ["46"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["461", "4610"],
      "nace_codes": ["46.1"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["462", "4620"],
      "nace_codes": ["46.2"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["463", "4630"],
      "nace_codes": ["46.3"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["464"],
      "nace_codes": ["46.4"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4641"],
      "nace_codes": ["46.41", "46.42"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4642"],
      "nace_codes": ["46.47"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4649"],
      "nace_codes": ["46.43", "46.44", "46.45", "46.46", "46.48", "46.49"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["465"],
      "nace_codes": ["46.5", "46.6"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4651"],
      "nace_codes": ["46.50"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4652"],
      "nace_codes": ["46.50"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4653"],
      "nace_codes": ["46.61"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4659"],
      "nace_codes": ["46.62", "46.63", "46.64"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["466"],
      "nace_codes": ["46.7"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4661"],
      "nace_codes": ["46.71"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4662"],
      "nace_codes": ["46.72"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4663"],
      "nace_codes": ["46.73"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["467"],
      "nace_codes": ["46.8"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4671"],
      "nace_codes": ["46.81"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4672"],
      "nace_codes": ["46.82"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4673"],
      "nace_codes": ["46.83", "46.84"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4679"],
      "nace_codes": ["46.85", "46.86", "46.87", "46.89"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["469", "4690"],
      "nace_codes": ["46.9", "46.90"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["47"],
      "nace_codes": ["47"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["471"],
      "nace_codes": ["47.1"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4711"],
      "nace_codes": ["47.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4719"],
      "nace_codes": ["47.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["472"],
      "nace_codes": ["47.2"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4721"],
      "nace_codes": ["47.21", "47.22", "47.23", "47.24", "47.27"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4722"],
      "nace_codes": ["47.25"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4723"],
      "nace_codes": ["47.26"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["473", "4730"],
      "nace_codes": ["47.3", "47.30"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["474", "4740"],
      "nace_codes": ["47.4", "47.40"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["475"],
      "nace_codes": ["47.5"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4751"],
      "nace_codes": ["47.51"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4752"],
      "nace_codes": ["47.52"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4753"],
      "nace_codes": ["47.53"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4759"],
      "nace_codes": ["47.54", "47.55"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["476"],
      "nace_codes": ["47.6"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4761"],
      "nace_codes": ["47.61", "47.62"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4762"],
      "nace_codes": ["47.63"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4763"],
      "nace_codes": ["47.64"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4769"],
      "nace_codes": ["47.69"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["477"],
      "nace_codes": ["47.7"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4771"],
      "nace_codes": ["47.71", "47.72"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4772"],
      "nace_codes": ["47.73", "47.74", "47.75"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4773"],
      "nace_codes": ["47.76", "47.77", "47.78"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["4774"],
      "nace_codes": ["47.79"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["478"],
      "nace_codes": ["47.8"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4781"],
      "nace_codes": ["47.81"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4782"],
      "nace_codes": ["47.82"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["4783"],
      "nace_codes": ["47.83"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["479", "4790"],
      "nace_codes": ["47.9"],
      "confidence": "High",
      "match_type": "many-to-one"
    }
  ],
  "unmatched_codes": {
    "isic": [],
    "nace": ["46.11", "46.12", "46.13", "46.14", "46.15", "46.16", "46.17", "46.18", "46.19", "46.21", "46.22", "46.23", "46.24", "46.31", "46.32", "46.33", "46.34", "46.35", "46.36", "46.37", "46.38", "46.39", "47.91", "47.92"]
  }
}
```

**Analysis Notes:**

1.  **High-Level Structure:** The mapping is straightforward at the Section (G) and Division (46, 47) levels, with a **one-to-one** correspondence and **High** confidence.
2.  **Granularity Difference:** NACE is significantly more detailed, especially in:
    *   **Wholesale Agents (46.1):** ISIC has a single class `4610`. NACE breaks this down into many specific agent classes (`46.11` to `46.19`) based on the product type. This results in a **many-to-one** mapping from ISIC to NACE.
    *   **Retail Intermediation (47.9):** Similarly, ISIC's `4790` is split in NACE into `47.91` (non-specialised) and `47.92` (specialised).
    *   **Product Categories:** Throughout the classifications, NACE often splits a broader ISIC class into multiple, more specific ones (e.g., `ISIC 4649` maps to **six** NACE classes). This is the most common pattern, resulting in **one-to-many** mappings.
3.  **Unmatched NACE Codes:** The `"unmatched_codes"` list contains all the NACE classes that are subdivisions of the broader ISIC categories. They are not "unmatched" in the sense of having no corresponding activity in ISIC; rather, they represent the finer European detail within the ISIC framework. For a complete correspondence, each of these NACE codes would map **up** to its parent ISIC code as shown in the mappings list.
4.  **Confidence:** Confidence is rated **High** for all mappings because the systems are directly aligned, with NACE being a regional elaboration of ISIC. The titles, descriptions, and hierarchical logic are semantically identical, with differences only in the level of detail.