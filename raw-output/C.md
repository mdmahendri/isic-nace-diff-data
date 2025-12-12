Based on my analysis of the provided ISIC and NACE classification data, here is the correspondence mapping. The analysis focused on the hierarchical structure, semantic similarity of titles and descriptions, and cross-references within the systems. NACE is generally more granular than ISIC, leading to many one-to-many matches.

```json
{
  "mappings": [
    {
      "isic_codes": ["C"],
      "nace_codes": ["C"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["10"],
      "nace_codes": ["10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["101", "1010"],
      "nace_codes": ["10.1", "10.11", "10.12", "10.13"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["102", "1020"],
      "nace_codes": ["10.2", "10.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["103", "1030"],
      "nace_codes": ["10.3", "10.31", "10.32", "10.39"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["104", "1040"],
      "nace_codes": ["10.4", "10.41", "10.42"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["105", "1050"],
      "nace_codes": ["10.5", "10.51"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["106"],
      "nace_codes": ["10.6"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1061"],
      "nace_codes": ["10.61"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1062"],
      "nace_codes": ["10.62"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["107"],
      "nace_codes": ["10.7", "10.8"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1071"],
      "nace_codes": ["10.71", "10.72"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1072"],
      "nace_codes": ["10.81"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1073"],
      "nace_codes": ["10.82"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1074"],
      "nace_codes": ["10.73"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1075"],
      "nace_codes": ["10.85"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1076"],
      "nace_codes": ["10.83"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1079"],
      "nace_codes": ["10.84", "10.86", "10.89"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["108", "1080"],
      "nace_codes": ["10.9", "10.91", "10.92"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["11"],
      "nace_codes": ["11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1101"],
      "nace_codes": ["11.01"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1102"],
      "nace_codes": ["11.02", "11.03", "11.04"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1103"],
      "nace_codes": ["11.05"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1104"],
      "nace_codes": ["11.06"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1105"],
      "nace_codes": ["11.07"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["12", "120", "1200"],
      "nace_codes": ["12", "12.0", "12.00"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["13"],
      "nace_codes": ["13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1311"],
      "nace_codes": ["13.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1312"],
      "nace_codes": ["13.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1313"],
      "nace_codes": ["13.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1391"],
      "nace_codes": ["13.91"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1392"],
      "nace_codes": ["13.92"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1393"],
      "nace_codes": ["13.93"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1394"],
      "nace_codes": ["13.94"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1399"],
      "nace_codes": ["13.95", "13.96", "13.99"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["14"],
      "nace_codes": ["14"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["141", "1410"],
      "nace_codes": ["14.2", "14.21", "14.22", "14.23", "14.29"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["142", "1420"],
      "nace_codes": ["14.24"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["143", "1430"],
      "nace_codes": ["14.1", "14.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["15"],
      "nace_codes": ["15"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1511"],
      "nace_codes": ["15.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1512"],
      "nace_codes": ["15.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["152", "1520"],
      "nace_codes": ["15.2", "15.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["16"],
      "nace_codes": ["16"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["161", "1610"],
      "nace_codes": ["16.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1621"],
      "nace_codes": ["16.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1622"],
      "nace_codes": ["16.22", "16.23", "16.25"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1623"],
      "nace_codes": ["16.24"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1629"],
      "nace_codes": ["16.12", "16.26", "16.27", "16.28"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["17"],
      "nace_codes": ["17"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1701"],
      "nace_codes": ["17.11", "17.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1702"],
      "nace_codes": ["17.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1709"],
      "nace_codes": ["17.22", "17.23", "17.24", "17.25"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["18"],
      "nace_codes": ["18"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["1811"],
      "nace_codes": ["18.11", "18.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["1812"],
      "nace_codes": ["18.13", "18.14"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["182", "1820"],
      "nace_codes": ["18.2", "18.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["19"],
      "nace_codes": ["19"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["191", "1910"],
      "nace_codes": ["19.1", "19.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["192", "1920"],
      "nace_codes": ["19.2", "19.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["20"],
      "nace_codes": ["20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2011"],
      "nace_codes": ["20.11", "20.12", "20.13", "20.14"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2012"],
      "nace_codes": ["20.15"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2013"],
      "nace_codes": ["20.16", "20.17"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2021"],
      "nace_codes": ["20.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2022"],
      "nace_codes": ["20.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2023"],
      "nace_codes": ["20.41", "20.42"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2029"],
      "nace_codes": ["20.51", "20.59"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["203", "2030"],
      "nace_codes": ["20.6", "20.60"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["21", "210", "2100"],
      "nace_codes": ["21", "21.1", "21.10", "21.2", "21.20"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["22"],
      "nace_codes": ["22"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2211"],
      "nace_codes": ["22.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2219"],
      "nace_codes": ["22.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["222", "2220"],
      "nace_codes": ["22.2", "22.21", "22.22", "22.23", "22.24", "22.25", "22.26"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["23"],
      "nace_codes": ["23"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["231", "2310"],
      "nace_codes": ["23.1", "23.11", "23.12", "23.13", "23.14", "23.15"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2391"],
      "nace_codes": ["23.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2392"],
      "nace_codes": ["23.3", "23.31", "23.32"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2393"],
      "nace_codes": ["23.4", "23.41", "23.42", "23.43", "23.44", "23.45"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2394"],
      "nace_codes": ["23.5", "23.51", "23.52"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2395"],
      "nace_codes": ["23.6", "23.61", "23.62", "23.63", "23.64", "23.65", "23.66"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2396"],
      "nace_codes": ["23.7", "23.70"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2399"],
      "nace_codes": ["23.9", "23.91", "23.99"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["24"],
      "nace_codes": ["24"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["241", "2410"],
      "nace_codes": ["24.1", "24.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["242", "2420"],
      "nace_codes": ["24.4", "24.41", "24.42", "24.43", "24.44", "24.45", "24.46"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2431"],
      "nace_codes": ["24.51", "24.52"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2432"],
      "nace_codes": ["24.53", "24.54"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["25"],
      "nace_codes": ["25"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2511"],
      "nace_codes": ["25.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2512"],
      "nace_codes": ["25.22"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2513"],
      "nace_codes": ["25.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["252", "2520"],
      "nace_codes": ["25.3", "25.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2591"],
      "nace_codes": ["25.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2592"],
      "nace_codes": ["25.5", "25.51", "25.52", "25.53"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2593"],
      "nace_codes": ["25.6", "25.61", "25.62", "25.63"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2599"],
      "nace_codes": ["25.9", "25.91", "25.92", "25.93", "25.94", "25.99"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["26"],
      "nace_codes": ["26"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2611"],
      "nace_codes": ["26.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2619"],
      "nace_codes": ["26.11", "26.12"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["262", "2620"],
      "nace_codes": ["26.2", "26.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["263", "2630"],
      "nace_codes": ["26.3", "26.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["264", "2640"],
      "nace_codes": ["26.4", "26.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2651"],
      "nace_codes": ["26.51"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2652"],
      "nace_codes": ["26.52"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["266", "2660"],
      "nace_codes": ["26.6", "26.60"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["267", "2670"],
      "nace_codes": ["26.7", "26.70"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["268", "2680"],
      "nace_codes": ["26.70"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["27"],
      "nace_codes": ["27"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["271", "2710"],
      "nace_codes": ["27.1", "27.11", "27.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["272", "2720"],
      "nace_codes": ["27.2", "27.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2731"],
      "nace_codes": ["27.31"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2732"],
      "nace_codes": ["27.32"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2733"],
      "nace_codes": ["27.33"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["274", "2740"],
      "nace_codes": ["27.4", "27.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["275", "2750"],
      "nace_codes": ["27.5", "27.51", "27.52"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["279", "2790"],
      "nace_codes": ["27.9", "27.90"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["28"],
      "nace_codes": ["28"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2811"],
      "nace_codes": ["28.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2812"],
      "nace_codes": ["28.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2813"],
      "nace_codes": ["28.13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2814"],
      "nace_codes": ["28.15"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2815"],
      "nace_codes": ["28.21"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2816"],
      "nace_codes": ["28.22"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2817"],
      "nace_codes": ["28.23"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2818"],
      "nace_codes": ["28.24"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2819"],
      "nace_codes": ["28.25", "28.29"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2821"],
      "nace_codes": ["28.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2822"],
      "nace_codes": ["28.4", "28.41", "28.42"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["2823"],
      "nace_codes": ["28.91"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2824"],
      "nace_codes": ["28.92"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2825"],
      "nace_codes": ["28.93"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2826"],
      "nace_codes": ["28.94"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["2829"],
      "nace_codes": ["28.95", "28.96", "28.97", "28.99"],
      "confidence": "Medium",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["29"],
      "nace_codes": ["29"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["291", "2910"],
      "nace_codes": ["29.1", "29.10"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["292", "2920"],
      "nace_codes": ["29.2", "29.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["293", "2930"],
      "nace_codes": ["29.3", "29.31", "29.32"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["30"],
      "nace_codes": ["30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3011"],
      "nace_codes": ["30.11", "30.13"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["3012"],
      "nace_codes": ["30.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["302", "3020"],
      "nace_codes": ["30.2", "30.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["303", "3030"],
      "nace_codes": ["30.3", "30.31", "30.32"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["304", "3040"],
      "nace_codes": ["30.4", "30.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3091"],
      "nace_codes": ["30.91"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3092"],
      "nace_codes": ["30.92"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3099"],
      "nace_codes": ["30.99"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["31"],
      "nace_codes": ["31"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3101"],
      "nace_codes": ["31.00"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3102"],
      "nace_codes": ["31.00"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["32"],
      "nace_codes": ["32"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3211"],
      "nace_codes": ["32.11", "32.12"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["3212"],
      "nace_codes": ["32.13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["322", "3220"],
      "nace_codes": ["32.2", "32.20"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["323", "3230"],
      "nace_codes": ["32.3", "32.30"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["324", "3240"],
      "nace_codes": ["32.4", "32.40"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["325", "3250"],
      "nace_codes": ["32.5", "32.50"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["329", "3290"],
      "nace_codes": ["32.9", "32.91", "32.99"],
      "confidence": "High",
      "match_type": "one-to-many"
    },
    {
      "isic_codes": ["33"],
      "nace_codes": ["33"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3311"],
      "nace_codes": ["33.11"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3312"],
      "nace_codes": ["33.12"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
    {
      "isic_codes": ["3313"],
      "nace_codes": ["33.13"],
      "confidence": "High",
      "match_type": "one-to-one"
    },
   