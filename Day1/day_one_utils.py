import pandas as pd

START_VALUE = 50
DATA_PATH = "data/input1.csv"

def read_puzzle_input(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = ['input']
    return df

def split_puzzle_input(df: pd.DataFrame) -> pd.DataFrame:
    df['LR'], df['turn_distance'] = df['input'].str[0], df['input'].str[1:].astype(int)
    df['turn_right'] = df['LR'].map(lambda x: True if x == 'R' else False)
    return df

def prepare_data()-> pd.DataFrame:
    return split_puzzle_input(split_puzzle_input(read_puzzle_input(DATA_PATH)))
