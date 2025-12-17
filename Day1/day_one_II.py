import math

from day_one_utils import START_VALUE, prepare_data

def calc_result_of_rotation(cur : int, turn_distance : int) -> int:
    return (cur + turn_distance) % 100

def get_passes_right_turns(current_position : int, turn_distance : int):
    return math.trunc((current_position + turn_distance) / 100)

def get_passes_left_turns(current_position : int, turn_distance : int):
    # if the position is 0 then that was already counted
    if current_position != 0:
        # check if 0 was passed at all
        if current_position + turn_distance > 0:
            return 0
        # add one for first pass!!
        return abs(math.trunc((current_position + turn_distance) / 100)) + 1
    return abs(math.trunc((current_position + turn_distance) / 100))

def calc_password(turns: list[tuple[int, bool]]) -> int:
    first = True
    current = START_VALUE
    password = 0
    for turn in turns:
        turn_distance = turn[0]
        turn_right = turn[1]
        if turn_right:
            password += get_passes_right_turns(current, turn_distance)
        else:
            turn_distance = -turn_distance
            password += get_passes_left_turns(current, turn_distance)
        current = calc_result_of_rotation(START_VALUE if first else current, turn_distance)
        if first:
            first = False
    return password

def main() -> None:
    df = prepare_data()
    password = calc_password(zip(df.turn_distance, df.turn_right))
    print(password)

if __name__ == "__main__":
    main()




