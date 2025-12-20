import re

DATA_PATH = "data/input.txt"

def read_input():
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        joltage_banks = [list(line) for line in lines]
        joltage_banks = [list(map(int, x)) for x in joltage_banks]
        return joltage_banks