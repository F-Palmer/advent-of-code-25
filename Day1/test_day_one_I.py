import unittest
from day_one_I import calc_result_of_rotation, calc_password

class TestCalcResultOfRotation(unittest.TestCase):
    def test_standard_case(self):
        current_position = 50
        turn_distance = 25
        turn_right = False
        result = calc_result_of_rotation(current_position, turn_distance, turn_right)
        self.assertEqual(result, 25)

    def test_wrap(self):
        current_position = 50
        turn_distance = 56
        turn_right = True
        result = calc_result_of_rotation(current_position, turn_distance, turn_right)
        self.assertEqual(result, 6)

    def test_edge_case1(self):
        current_position = 50
        turn_distance = 50
        turn_right = True
        result = calc_result_of_rotation(current_position, turn_distance, turn_right)
        self.assertEqual(result, 0)

    def test_edge_case2(self):
        current_position = 50
        turn_distance = 50
        turn_right = False
        result = calc_result_of_rotation(current_position, turn_distance, turn_right)
        self.assertEqual(result, 0)

class TestCalcPassword(unittest.TestCase):
    def test_standard_case(self):
        turns = [
            (25, True),
            (75, False),
            (100, True),
            (12, False)
        ]
        result = calc_password(turns)
        self.assertEqual(result, 2)

    def test_no_hits(self):
        turns = [
            (24, False),
            (75, False),
            (100, False),
        ]
        result = calc_password(turns)
        self.assertEqual(result, 0)



if __name__ == "__main__":
    unittest.main()
