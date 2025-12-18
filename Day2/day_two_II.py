import pandas as pd
import math
import textwrap

from day_two_utils import read_input

# performance increase idea: Look-up table
def get_possible_lengths_of_pattern(number_length: int)-> list[int]:
    possible_lengths = list(range(1, math.floor(number_length/2)+ 1) )
    copy_possible_lengths = possible_lengths.copy()
    for length in copy_possible_lengths:
        if (number_length / length) % 1 != 0:
            possible_lengths.remove(length)
    return possible_lengths

def get_possible_patterns(number: str)-> list[str]:
    possible_lengths = get_possible_lengths_of_pattern(len(number))
    possible_patterns = []
    for length in possible_lengths:
        possible_patterns.append(number[:length])
    return possible_patterns

def check_if_patterns_apply(number: str, possible_patterns: list[str]) -> bool:
    # ignore 1 character numbers
    if len(number) == 1:
        return False
    # check longer patterns first
    for pattern in reversed(possible_patterns):
        chunks = textwrap.wrap(number, len(pattern))
        first = chunks[0]
        if all(first==x for x in chunks):
            return True
    return False

def sum_of_invalid_IDs(df: pd.DataFrame) -> int:
    sum_of_ids = 0
    for _, row in df.iterrows():
        for id in range(row['Start'], row['End']+1):
            if check_if_patterns_apply(str(id), get_possible_patterns(str(id))):
                sum_of_ids += id
    return sum_of_ids

def main():
    df = read_input()
    print(f"Sum of invalid IDs: {sum_of_invalid_IDs(df)}")

if __name__ == "__main__":
    main()


