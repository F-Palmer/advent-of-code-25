import pandas as pd
import math

from day_two_utils import read_input

def check_for_silly_pattern(number: str) -> bool:
    # pattern not possible on uneven lengths
    if len(number) % 2 != 0:
        return False
    # split down the middle
    first_part = number[:math.trunc(len(number) / 2)]
    second_part = number[math.trunc(len(number) / 2):]
    if first_part == second_part:
        return True
    return False

def sum_of_invalid_IDs(df: pd.DataFrame) -> int:
    sum_of_ids = 0
    for _, row in df.iterrows():
        for id in range(row['Start'], row['End']+1):
            if check_for_silly_pattern(str(id)):
                sum_of_ids += id

    return sum_of_ids

def main():
    df = read_input()
    print(f"Sum of invalid IDs: {sum_of_invalid_IDs(df)}")

if __name__ == "__main__":
    main()


