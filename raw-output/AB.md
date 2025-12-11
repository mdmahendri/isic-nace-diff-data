Looking at the provided data for Sections A and B, I can create a detailed mapping. The structures are extremely similar, with NACE being a more granular European adaptation of ISIC. The main differences are in the formatting of codes (ISIC uses 4-digit codes without decimals, NACE uses a decimal system) and some minor title variations and splits.

Here is the structured JSON mapping:

```json
{
  "mappings": [
    {
      "isic_codes": ["A"],
      "nace_codes": ["A"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["01"],
      "nace_codes": ["01"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["011"],
      "nace_codes": ["01.1"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0111"],
      "nace_codes": ["01.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0112"],
      "nace_codes": ["01.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0113"],
      "nace_codes": ["01.13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0114"],
      "nace_codes": ["01.14"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0115"],
      "nace_codes": ["01.15"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0116"],
      "nace_codes": ["01.16"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0119"],
      "nace_codes": ["01.19"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["012"],
      "nace_codes": ["01.2"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0121"],
      "nace_codes": ["01.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0122"],
      "nace_codes": ["01.22"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0123"],
      "nace_codes": ["01.23"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0124"],
      "nace_codes": ["01.24"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0125"],
      "nace_codes": ["01.25"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0126"],
      "nace_codes": ["01.26"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0127"],
      "nace_codes": ["01.27"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0128"],
      "nace_codes": ["01.28"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0129"],
      "nace_codes": ["01.29"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["013", "0130"],
      "nace_codes": ["01.3", "01.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["014"],
      "nace_codes": ["01.4"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0141"],
      "nace_codes": ["01.41", "01.42"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["0142"],
      "nace_codes": ["01.43"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0143"],
      "nace_codes": ["01.44"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0144"],
      "nace_codes": ["01.45"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0145"],
      "nace_codes": ["01.46"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0146"],
      "nace_codes": ["01.47"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0149"],
      "nace_codes": ["01.48"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["015", "0150"],
      "nace_codes": ["01.5", "01.50"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["016"],
      "nace_codes": ["01.6"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0161"],
      "nace_codes": ["01.61"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0162"],
      "nace_codes": ["01.62"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0163", "0164"],
      "nace_codes": ["01.63"],
      "confidence": "High",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["017", "0170"],
      "nace_codes": ["01.7", "01.70"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["02"],
      "nace_codes": ["02"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["021", "0210"],
      "nace_codes": ["02.1", "02.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["022", "0220"],
      "nace_codes": ["02.2", "02.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["023", "0230"],
      "nace_codes": ["02.3", "02.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["024", "0240"],
      "nace_codes": ["02.4", "02.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["03"],
      "nace_codes": ["03"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["031"],
      "nace_codes": ["03.1"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0311"],
      "nace_codes": ["03.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0312"],
      "nace_codes": ["03.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["032"],
      "nace_codes": ["03.2"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0321"],
      "nace_codes": ["03.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0322"],
      "nace_codes": ["03.22"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["033", "0330"],
      "nace_codes": ["03.3", "03.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["B"],
      "nace_codes": ["B"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["05"],
      "nace_codes": ["05"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["051", "0510"],
      "nace_codes": ["05.1", "05.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["052", "0520"],
      "nace_codes": ["05.2", "05.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["06"],
      "nace_codes": ["06"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["061", "0610"],
      "nace_codes": ["06.1", "06.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["062", "0620"],
      "nace_codes": ["06.2", "06.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["07"],
      "nace_codes": ["07"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["071", "0710"],
      "nace_codes": ["07.1", "07.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["072"],
      "nace_codes": ["07.2"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0721"],
      "nace_codes": ["07.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0729"],
      "nace_codes": ["07.29"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["08"],
      "nace_codes": ["08"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["081", "0810"],
      "nace_codes": ["08.1"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["089"],
      "nace_codes": ["08.9"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0891"],
      "nace_codes": ["08.91"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0892"],
      "nace_codes": ["08.92"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0893"],
      "nace_codes": ["08.93"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["0899"],
      "nace_codes": ["08.99"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["09"],
      "nace_codes": ["09"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["091", "0910"],
      "nace_codes": ["09.1", "09.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["099", "0990"],
      "nace_codes": ["09.9", "09.90"],
      "confidence": "High",
      "match_type": "one-to-one"
    }
  ],
  "unmatched_codes": {
    "isic": [],
    "nace": ["08.11", "08.12"]
  }
}
```

### Key Observations and Rationale:

1.  **High Confidence Matches:** The vast majority of codes are direct, one-to-one matches with identical or nearly identical titles. The hierarchical structure (Sections, Divisions, Groups, Classes) aligns perfectly.
2.  **Notable Exceptions (Medium Confidence):**
    *   **ISIC 0141 (Raising of cattle and buffaloes)** maps to **NACE 01.41 (Raising of dairy cattle)** and **01.42 (Raising of other cattle and buffaloes)**. NACE splits this category, so it's a one-to-many match. The semantic coverage is complete, but the granularity differs.
    *   **ISIC 081/0810 (Quarrying of stone, sand and clay)** maps to the broader **NACE 08.1**. NACE provides more detail with **08.11** and **08.12**. This is a one-to-many match where the ISIC code is less granular.
3.  **Consolidation (High Confidence):**
    *   **ISIC 0163 (Post-harvest crop activities)** and **0164 (Seed processing for propagation)** are consolidated into a single **NACE 01.63 (Post-harvest crop activities and seed processing for propagation)**. This is a clear many-to-one match.
4.  **Unmatched NACE Codes:** **NACE 08.11** and **08.12** are more detailed sub-categories of the ISIC 081 group. They are listed as unmatched because there is no single, equally granular ISIC code to map them to individually. They are correctly covered by the mapping to the parent code `08.1`.
5.  **Code Format:** ISIC codes in the 4th digit (e.g., `0130`) often represent the same activity as the 3-digit group (e.g., `013`). In these cases, both are mapped to the corresponding NACE group and class for completeness. NACE uses a consistent decimal system (e.g., `01.30`).

This mapping for Sections A and B is highly reliable due to the structural and semantic alignment between the two systems.