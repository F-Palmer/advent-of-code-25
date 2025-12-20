import copy

from day_four_utils import read_data


def display_warehouse(ware_house):
    for row in ware_house:
        print(''.join(row))

def is_center_tile_reachable(row: int, column: int, ware_house: list[list[str]]) -> bool:
    paper_rolls = 0
    for x in [-1,0, 1]:
        for y in [-1,0, 1]:
            if x == 0 and y == 0:
                continue
            if ware_house[row + x][column + y] == "@":
                paper_rolls += 1
    if paper_rolls > 3:
        return False
    return True

def get_number_reachable(ware_house: list[list[str]]) -> tuple[int, list[list[str]]]:
    reachable = 0
    copy_ware_house = copy.deepcopy(ware_house)
    for x in range(1, len(ware_house)-1):
        for y in range(1, len(ware_house)-1):
            if ware_house[x][y] == "@":
                if is_center_tile_reachable(x, y, ware_house):
                    reachable += 1
                    copy_ware_house[x][y] = "."
    return reachable, copy_ware_house

def get_total_number_reachable(ware_house: list[list[str]]) -> int:
    total_reachable = 0
    reachable = 0
    stop = False
    while not stop:
        reachable, ware_house = get_number_reachable(ware_house)
        if reachable == 0:
            stop = True
        total_reachable += reachable
    display_warehouse(ware_house)
    return total_reachable


def expand_borders(ware_house):
    length_of_column = len(ware_house[0])
    # add empty line in first and last position
    ware_house.insert(0, ['.'] * length_of_column)
    ware_house.append(['.'] * length_of_column)
    # add empty fields at beginning and end of each row
    length_of_row = len(ware_house)
    for i in range(length_of_row):
        ware_house[i].append('.')
        ware_house[i].insert(0, '.')
    return ware_house



def main():
    ware_house = read_data()
    ware_house = expand_borders(ware_house)
    display_warehouse(ware_house)
    print(get_total_number_reachable(ware_house))

if __name__ == '__main__':
    main()