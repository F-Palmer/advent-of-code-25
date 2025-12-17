import unittest
from day_one_II import calc_result_of_rotation, calc_password


class TestCalcResultOfRotation(unittest.TestCase):
    def test_standard_case(self):
        current_position = 50
        turn_distance = -25
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 25)

    def test_wrap(self):
        current_position = 50
        turn_distance = 56
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 6)

    def test_edge_case1(self):
        current_position = 50
        turn_distance = 50
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 0)

    def test_edge_case2(self):
        current_position = 50
        turn_distance = -50
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 0)

    def test_large_case1(self):
        current_position = 50
        turn_distance = 469
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 19)

    def test_edge_case2(self):
        current_position = 50
        turn_distance = -469
        result = calc_result_of_rotation(current_position, turn_distance)
        self.assertEqual(result, 81)


class TestCalcPassword(unittest.TestCase):
    def test_standard_case(self):
        turns = [
            (75, True),
        ]
        result = calc_password(turns)
        self.assertEqual(result, 1)

    def test_large_addition(self):
        turns = [
            (25, True),
            (300, True),
        ]
        result = calc_password(turns)
        self.assertEqual(result, 3)

    def test_small_subtraction(self):
        turns = [
            (75, False),
        ]
        result = calc_password(turns)
        self.assertEqual(1, result)

    def test_large_subtraction(self):
        turns = [
            (300, False),
        ]
        result = calc_password(turns)
        self.assertEqual(3, result)

    def test_exactly_zero_subtraction(self):
        turns = [
            (49, False),
            (201, False)
        ]
        result = calc_password(turns)
        self.assertEqual(3, result)

    def test_exactly_zero_addition(self):
        turns = [
            (50, True),
            (50, True),
            (250, True)
        ]
        result = calc_password(turns)
        self.assertEqual(4, result)

    def test_many_wraps(self):
        turns = [
            (11, False)
        ] * 20
        result = calc_password(turns)
        self.assertEqual(2, result)


    def test_AoC_example(self):
        print("Starting AOC example")
        turns = [
            (68, False),
            (30, False),
            (48, True),
            (5, False),
            (60, True),
            (55, False),
            (1, False),
            (99, False),
            (14, True),
            (82, False)
        ]
        result = calc_password(turns)
        self.assertEqual(6, result)


if __name__ == "__main__":
    unittest.main()
