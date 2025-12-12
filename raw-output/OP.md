Based on my analysis of the provided ISIC and NACE codes, here is the correspondence mapping. The analysis focused on semantic similarity in titles and descriptions, hierarchical structure, and the principle that NACE is a more granular European adaptation of ISIC.

```json
{
  "mappings": [
    {
      "isic_codes": ["O"],
      "nace_codes": ["O"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["77"],
      "nace_codes": ["77"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["771", "7710"],
      "nace_codes": ["77.1", "77.11", "77.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["772", "7721", "7729"],
      "nace_codes": ["77.2", "77.21", "77.22"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["773", "7730"],
      "nace_codes": ["77.3", "77.31", "77.32", "77.33", "77.34", "77.35", "77.39"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["774", "7740"],
      "nace_codes": ["77.4", "77.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["775", "7751", "7752"],
      "nace_codes": ["77.5", "77.51", "77.52"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["78"],
      "nace_codes": ["78"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["781", "7810"],
      "nace_codes": ["78.1", "78.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["782", "7820"],
      "nace_codes": ["78.2", "78.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["79"],
      "nace_codes": ["79"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["791", "7911", "7912"],
      "nace_codes": ["79.1", "79.11", "79.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["799", "7990"],
      "nace_codes": ["79.9", "79.90"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["80"],
      "nace_codes": ["80"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["801", "8011"],
      "nace_codes": ["80.0", "80.01"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["8019"],
      "nace_codes": ["80.09"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["81"],
      "nace_codes": ["81"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["811", "8110"],
      "nace_codes": ["81.1", "81.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["812", "8121", "8129"],
      "nace_codes": ["81.2", "81.21", "81.22", "81.23"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["813", "8130"],
      "nace_codes": ["81.3", "81.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["82"],
      "nace_codes": ["82"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["821", "8210"],
      "nace_codes": ["82.1", "82.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["822", "8220"],
      "nace_codes": ["82.2", "82.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["823", "8230"],
      "nace_codes": ["82.3", "82.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["824", "8240"],
      "nace_codes": ["82.4", "82.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["829", "8291", "8292", "8299"],
      "nace_codes": ["82.9", "82.91", "82.92", "82.99"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["P"],
      "nace_codes": ["P"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["84"],
      "nace_codes": ["84"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["841", "8411"],
      "nace_codes": ["84.1", "84.11"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["8412"],
      "nace_codes": ["84.12"],
      "confidence": "Medium",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["8413"],
      "nace_codes": ["84.12"],
      "confidence": "Medium",
      "match_type": "many-to-one"
    },
    {
      "isic_codes": ["8414"],
      "nace_codes": ["84.13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["842", "8421", "8422", "8423"],
      "nace_codes": ["84.2", "84.21", "84.22", "84.23", "84.24", "84.25"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["843", "8430"],
      "nace_codes": ["84.3", "84.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    }
  ],
  "unmatched_codes": {
    "isic": [],
    "nace": []
  }
}
```

**Key Observations and Explanations:**

1.  **High-Level Correspondence:** The section (`O`, `P`) and division (`77`, `78`, `79`, `80`, `81`, `82`, `84`) codes show a perfect one-to-one match, confirming NACE's basis in ISIC.
2.  **Granularity:** NACE is consistently more detailed. This is most evident in:
    *   **Rental of Motor Vehicles (77.1):** NACE splits this into light vehicles (`77.11`) and trucks (`77.12`), while ISIC has a single class (`7710`).
    *   **Rental of Other Machinery (77.3):** NACE has six detailed subclasses (`77.31` to `77.39`), whereas ISIC has one (`7730`).
    *   **Cleaning Activities (81.2):** NACE distinguishes between general building cleaning (`81.21`), other building/industrial cleaning (`81.22`), and other cleaning (`81.23`). ISIC has general (`8121`) and other (`8129`).
    *   **Public Administration (84.2):** NACE further splits "Public order and safety" into Justice (`84.23`), Public Order (`84.24`), and Fire Services (`84.25`), which are combined in ISIC's `8423`.
3.  **Notable Structural Difference (Medium Confidence):** The mapping for environmental and social services regulation shows a structural divergence.
    *   **ISIC `8413` (Regulation of environmental services)** maps to **NACE `84.12`**. This is because NACE `84.12` combines the regulation of social services *and* environmental services, which are separate in ISIC (`8412` and `8413`). Therefore, ISIC `8412` and `8413` both map to NACE `84.12` (a many-to-one relationship). The confidence is Medium because the scope of NACE `84.12` is broader.
4.  **Semantic Matching:** Titles and descriptions are nearly identical, often verbatim, indicating a direct translation/adaptation process. Exclusions and inclusions are also highly aligned.
5.  **Complete Coverage:** All provided ISIC and NACE codes have been successfully matched. The `unmatched_codes` arrays are empty because the provided data sets are perfectly aligned subsets of the two systems for these sections.