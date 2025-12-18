import pandas as pd
from IPython.core.display_functions import display

DATA_PATH = "data/input.txt"

def read_input() -> pd.DataFrame:
    with open(DATA_PATH) as file:
        line = file.readline()
        number_ranges = line.split(',')
        df = pd.DataFrame(number_ranges)
        df.columns = ['number_range']
        df = df['number_range'].str.split('-', expand=True)
        df.columns = ['Start', 'End']
        df["Start"] = df["Start"].astype(int)
        df["End"] = df["End"].astype(int)
        return df


display(read_input())

