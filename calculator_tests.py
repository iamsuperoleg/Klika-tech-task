# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

try:
    from logger import logger
    from initializing import Initializing
except ImportError as e:
    print ("Error! {}. Check if file exists".format(e))
    Initialising = None


class CalculatorTests(unittest.TestCase, Initialising):
    def setUp(self):
        self.setup()

    def test_insert_digits(self):
        """Check inserting all digits 1234567890"""
        result = 1234567890
        buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_simple_multiplication(self):
        """Check 2 x 3 = 6"""
        result = 2 * 3
        buttons = ["2", "x", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_complicated_multiplication(self):
        """Check 25 x 15 x 5 = 1875"""
        result = 25 * 15 * 5
        buttons = ["2", "5", "x", "1", "5", "x", "5", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_simple_division(self):
        """Check 6 / 2 = 3"""
        result = 6 / 2
        buttons = ["6", "/", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_complicated_division(self):
        """Check 1875 / 5 / 15 = 25"""
        result = (1875 / 5) / 15
        buttons = ["1", "8", "7", "5", "/", "5", "/", "1", "5", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_simple_summation(self):
        """Check 1 + 3 = 4"""
        result = 1 + 3
        buttons = ["1", "+", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_complicated_summation(self):
        """Check 25 + 15 + 75 = 115"""
        result = 25 + 15 + 75
        buttons = ["2", "5", "+", "1", "5", "+", "7", "5", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_simple_subtraction(self):
        """Check 5 - 3 = 2"""
        result = 5 - 3
        buttons = ["5", "-", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_complicated_subtraction(self):
        """Check 115 - 25 - 15 = 75"""
        result = 115 - 25 - 15
        buttons = ["1", "1", "5", "-", "2", "5", "-", "1", "5", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_insert_float_without_zero_in_the_beginning(self):
        """Check inserting float without zero in the beginning 0.123456789"""
        result = 0.123456789
        buttons = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_insert_float_with_zero_in_the_beginning(self):
        """Check inserting float with zero in the beginning 0.123456789"""
        result = 0.123456789
        buttons = ["0", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_summation_of_floats(self):
        """Check 1.5 + 2.6 = 4.1"""
        result = 4.1
        buttons = ["1", ".", "5", "+", "2", ".", "6", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_subtraction_of_floats(self):
        """Check 1.5 - 2.6 = -1.1"""
        result = - 1.1
        buttons = ["1", ".", "5", "-", "2", ".", "6", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_multiplication_of_floats(self):
        """Check 2.5 * 0.5 = 1.25"""
        result = 1.25
        buttons = ["2", ".", "5", "x", "0", ".", "5", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_division_of_floats(self):
        """Check 2.5 / 0.4 = 6.25"""
        result = 6.25
        buttons = ["2", ".", "5", "/", "0", ".", "4", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_summation_and_subtraction(self):
        """Check 1 + 3 - 2 = 2"""
        result = 1 + 3 - 2
        buttons = ["1", "+", "3", "-", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_summation_and_multiplication(self):
        """Check 1 + 3 x 2 = 7"""
        result = 1 + 3 * 2
        buttons = ["1", "+", "3", "x", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_multiplication_and_summation(self):
        """Check 3 x 2 + 1 = 7"""
        result = 3 * 2 + 1
        buttons = ["3", "x", "2", "+", "1", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_summation_and_division(self):
        """Check 1 + 4 / 2 = 3"""
        result = 1 + 4 / 2
        buttons = ["1", "+", "4", "/", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_division_and_summation(self):
        """Check 4 / 2 + 1 = 3"""
        result = 4 / 2 + 1
        buttons = ["4", "/", "2", "+", "1", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_subtraction_and_multiplication(self):
        """Check 4 - 1 x 2 = 2"""
        result = 4 - 1 * 2
        buttons = ["4", "-", "1", "x", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_multiplication_and_subtraction(self):
        """Check 1 x 2 - 4 = -2"""
        result = 1 * 2 - 4
        buttons = ["1", "x", "2", "-", "4", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_subtraction_and_division(self):
        """Check 8 - 4 / 2 = 6"""
        result = 8 - 4 / 2
        buttons = ["8", "-", "4", "/", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_division_and_subtraction(self):
        """Check 8 / 2 - 6 = -2"""
        result = 8 / 2 - 6
        buttons = ["8", "x", "2", "-", "6", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_combination_of_division_and_multiplication(self):
        """Check 8 / 4 x 2 = 4"""
        result = 8 / 4 * 2
        buttons = ["8", "/", "4", "x", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_insert_negative(self):
        """Check inserting negative number -2"""
        result = - 2
        buttons = ["-", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_subtraction(self):
        """Check  - 2 - 4 = -6"""
        result = - 2 - 4
        buttons = ["-", "2", "-", "4", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_summation(self):
        """Check - 4 + 3 = -1"""
        result = - 4 + 3
        buttons = ["-", "4", "+", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_multiplication(self):
        """Check - 4 x 2 = -8"""
        result = - 4 * 2
        buttons = ["-", "4", "x", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_division(self):
        """Check - 4 / 2 = -2"""
        result = - 4 / 2
        buttons = ["-", "4", "/", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_on_negative_division(self):
        """Check - 4 / (- 2) = 2"""
        result = - 4 / - 2
        buttons = ["-", "4", "/", "-", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_negative_on_negative_multiplication(self):
        """Check - 4 x (- 2) = 8"""
        result = - 4 * (- 2)
        buttons = ["-", "4", "x", "-", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_check_C_button(self):
        """
        Click 3+2, click "C" button, click 3
        Expected result: 6
        """
        result = 6
        buttons = ["3", "+", "2", "C", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_check_AC_button(self):
        """
        Click 3 + 2
        Click "AC"
        Click +2x3 =
        Expected result: 6
        """
        result = 6
        buttons = ["3", "+", "2", "AC", "+", "2", "x", "3", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_division_by_zero(self):
        """
        Check division by zero: 2/0
        Expected result: Infinity
        """
        result = "Infinity"
        buttons = ["2", "/", "0", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def test_zero_division_by_digit(self):
        """Check 0 / 2 = 0"""
        result = 0 / 2
        buttons = ["0", "/", "2", "="]
        self.click_some_buttons(buttons)
        self.assertEqual(self.display(), str(result))

    def tearDown(self):
        self.teardown()


if __name__ == "__main__":
    date = datetime.now()
    dt = date.strftime("%H_%M_%S_%d.%m.%y")
    print ("{} - Starting tests".format(dt))
    results_file = open(dt + '_calculator_test_results.txt', 'w')
    unittest.main(testRunner=unittest.TextTestRunner(stream=results_file))
