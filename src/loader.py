import pandas as pd

def load_isic_nace_master():
    isic_df = pd.read_excel('../data/input/isic5codes.xlsx')
    nace_df = pd.read_excel('../data/input/nace21codes.xlsx')
    return isic_df, nace_df