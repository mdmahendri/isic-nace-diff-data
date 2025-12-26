import re
from pathlib import Path

import pandas as pd

from sentence_splitter import SentenceSplitter

def load_isic_nace_master():
    isic_df = pd.read_excel('../data/input/isic5codes.xlsx')
    nace_df = pd.read_excel('../data/input/nace21codes.xlsx')
    return isic_df, nace_df

def process_and_save_data(dataframe, output_dir, code_column, desc_column, lang='en'):
    """Process Excel data and save text files efficiently."""

    splitter = SentenceSplitter(language=lang)
    
    # Read data
    data = dataframe
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Process and write files
    for code, desc in zip(data[code_column], data[desc_column]):
        text = re.sub(r"[^\x00-\x7F]", "", desc) # non-ASCII characters like ñ and ü
        text = re.sub(r"[ \t]+", " ", text) # space or tab
        text = re.sub(r'\n+', '\n', text) # redundant newline
        text = re.sub(r"\.\s*\.", ".", text) # extra dot

        # Pattern 1: _x000D_ followed by list marker (-, •, *, number)
        # Keep as newline
        text = re.sub(r'_x000D_\s*(?=[-•*]|\d+\.)', '\n', text)
        
        # Pattern 2: _x000D_ followed by capital letter (new sentence)
        # Replace with period + newline or just newline
        text = re. sub(r'_x000D_\s*(?=[A-Z])', '.\n', text)
        
        # Pattern 3: _x000D_ within sentence (lowercase follows)
        # Replace with space
        text = re.sub(r'_x000D_\s*(?=[a-z])', ' ', text)
        
        # Pattern 4: _x000D_ at end (trailing)
        text = re.sub(r'_x000D_\s*$', '', text)
        
        # Clean up multiple periods
        text = re.sub(r'\.\.+', '.', text)

        paragraphs = '\n'.join(splitter.split(text))
        (output_path / f'{code}.txt').write_text(paragraphs, encoding='utf-8')