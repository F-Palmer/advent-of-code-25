import unittest

from day_three_I import find_all_highest_numbers

class TestFindAllHighestNumbers(unittest.TestCase):
    def test_single_value(self):
        input = [5]
        result = find_all_highest_numbers(input)
        self.assertEqual([0], result)

    def test_standard_single_case(self):
        input = [2, 1, 5, 8, 7]
        result = find_all_highest_numbers(input)
        self.assertEqual([3], result)

    def test_standard_multi_case(self):
        input = [2, 1, 5, 7, 3, 7]
        result = find_all_highest_numbers(input)
        self.assertEqual([3, 5], result)

if __name__ == '__main__':
    unittest.main()