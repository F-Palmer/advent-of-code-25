from day_three_utils import read_input

def find_all_highest_numbers(joltage_bank: list[int]) -> list[int]:
    indexes = []
    for possible_highest in reversed(range(1, 10)):
        for index, joltage in enumerate(joltage_bank):
            if joltage == possible_highest:
                indexes.append(index)
        if indexes:
            return indexes
    raise ValueError("No highest numbers found")

def joltage_of_bank(joltage_bank: list[int]) -> int:
    highest_number_indexes = find_all_highest_numbers(joltage_bank)
    highest_number = joltage_bank[highest_number_indexes[0]]
    # if the highest number exists more than once
    if len(highest_number_indexes) > 1:
        return highest_number*10 + highest_number
    # if the highest number is at the last position of the bank
    if highest_number_indexes[0] == len(joltage_bank)-1:
        next_highest_number_indexes = find_all_highest_numbers(joltage_bank[:-1])
        next_highest_number = joltage_bank[:-1][next_highest_number_indexes[0]]
        return next_highest_number*10 + highest_number
    if highest_number_indexes[0] == 0:
        next_highest_number_indexes = find_all_highest_numbers(joltage_bank[1:])
        next_highest_number = joltage_bank[1:][next_highest_number_indexes[0]]
        return highest_number*10 + next_highest_number
    # else: if there is only one highest number and its in the middle somewhere
    next_highest_number_indexes = find_all_highest_numbers(joltage_bank[highest_number_indexes[0]+1:])
    next_highest_number = joltage_bank[highest_number_indexes[0]+1:][next_highest_number_indexes[0]]
    return highest_number*10 + next_highest_number


def find_total_joltage(joltage_banks) -> int:
    total_joltage = 0
    for joltage_bank in joltage_banks:
        total_joltage += joltage_of_bank(joltage_bank)
    return total_joltage

def main():
    joltage_banks = read_input()
    print(find_total_joltage(joltage_banks))

if __name__ == "__main__":
    main()