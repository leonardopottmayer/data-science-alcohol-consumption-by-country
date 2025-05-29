import pandas as pd

def load_dataset() -> pd.DataFrame:
    datasetPath = '../data/drinks.csv'
    df = pd.read_csv(datasetPath)    
    return df
