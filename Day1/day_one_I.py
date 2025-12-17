from day_one_utils import START_VALUE, prepare_data

def calc_result_of_rotation(cur : int, turn_distance : int, turn_right : bool) -> int:
    """
    calculates the result of a turn of the vault dial, given its current positon
    """
    if turn_right:
        return (cur + turn_distance) % 100
    else:
        return abs((cur - turn_distance) % 100)

def calc_password(turns) -> int:
    first = True
    current = START_VALUE
    password = 0
    for turn in turns:
        turn_distance = turn[0]
        turn_right = turn[1]
        current = calc_result_of_rotation(START_VALUE if first else current, turn_distance, turn_right)
        if first:
            first = False
        if current == 0:
            password += 1
    return password


def main() -> None:
    df = prepare_data()
    password = calc_password(zip(df.turn_distance, df.turn_right))
    print(password)

if __name__ == "__main__":
    main()




