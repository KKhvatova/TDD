from unittest import TestCase
import calculator


class TestCalculator(TestCase):

    def test_add_function(self):
        cal = calculator.Calculator()
        self.assertEqual(cal.add_function(1, 2), 3)
        self.assertRaises(ValueError, cal.add_function, 1, 'a')

    def test_subtract_function(self):
        cal = calculator.Calculator()
        self.assertEqual(cal.subtract_function(2, 1), 1)
        self.assertRaises(ValueError, cal.subtract_function, 'a', 3)

    def test_division_function(self):
        cal = calculator.Calculator()
        self.assertEqual(cal.division_function(9, 3), 3)
        self.assertRaises(ValueError, cal.division_function, 7, 0)
