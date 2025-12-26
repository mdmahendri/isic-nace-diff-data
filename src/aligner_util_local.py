from pathlib import Path
import shutil

def copy_files_with_rename(cor_data, isic_dir, nace_dir, isic_dest, nace_dest):
    """Copy and rename files based on correspondence dataframe."""
    # Create destination directories
    Path(isic_dest).mkdir(parents=True, exist_ok=True)
    Path(nace_dest).mkdir(parents=True, exist_ok=True)
    
    for isic_code, nace_code in cor_data:
        new_name = f'{isic_code}_{nace_code}.txt'
        
        # Copy files
        shutil.copy(f'{isic_dir}{isic_code}.txt', f'{isic_dest}{new_name}')
        shutil.copy(f'{nace_dir}{nace_code}.txt', f'{nace_dest}{new_name}')