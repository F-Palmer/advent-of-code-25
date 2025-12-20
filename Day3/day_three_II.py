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

def get_best_number(joltage_bank: list[int]) -> tuple[int, int]:
    indexes = find_all_highest_numbers(joltage_bank)
    index = indexes[0]
    return index, joltage_bank[index]

def joltage_of_bank(joltage_bank: list[int]) -> int:
    last_selected_index = 0
    joltage = 0
    for x in reversed(range(0, 12)):
        # crop list to all values that are left of the number boundary (x) and are right of the last selected number
        current_crop = joltage_bank[last_selected_index:len(joltage_bank)-x]
        # find the highest left-most value in that remaining list
        idx_cur_best_num, cur_best_num = get_best_number(current_crop)
        joltage += cur_best_num * 10**x
        last_selected_index = last_selected_index+idx_cur_best_num+1
    return joltage
    # crop list to all values that are left of the 12 number boundary
    # find the highest left-most value in that remaining list
    # go to 11
    # crop list to all values that are left of the 11 number boundary and are right of the last selected number
    # ...



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