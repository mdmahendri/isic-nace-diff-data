def create_code_description(df, system_name):
    code_col = "ISIC5_Code" if system_name == "ISIC" else "CODE"
    title_col = "ISIC5_Title" if system_name == "ISIC" else "HEADING"
    desc_col = "ISIC5_Desc" if system_name == "ISIC" else "DESC"
    return [f"{system_name} Code: {row[code_col]} \n Title: {row[title_col]} \n Description: {row[desc_col]} \n" for _, row in df.iterrows()]