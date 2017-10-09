import unittest
from scripts import (
    convert
)


class BotTestCase(unittest.TestCase):

    # Tests for temperature conversion

    def test_convert_given_valid_inputs(self):
        self.assertEqual(convert(32, "F", "C"), 0)

    def test_convert_given_valid_inputs2(self):
        self.assertEqual(convert(32, "F", "K"), 273.15)

    def test_convert_given_invalid_unit(self):
        self.assertRaises(Exception, convert(10, "R", "F"))


if __name__ == '__main__':
    unittest.main()
