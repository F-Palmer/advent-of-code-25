DATA_PATH = "data/input.txt"

def read_data() -> list[list[str]]:
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        ware_house = [list(line) for line in lines]
        return ware_house
