import unittest
from binary_from_int import BinaryFromInt


class TestBinaryPy(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.binary_output = BinaryFromInt()

    def test_class(self):
        self.binary_output.number = 2
        self.assertIsNotNone(self.binary_output.number)

    def test_numeric(self):
        self.binary_output.number = '3.5'
        self.assertIsInstance(self.binary_output.number, int)

    def test_not_float(self):
        self.binary_output.number = 3.5
        self.assertNotIsInstance(self.binary_output.number, float)

    def test_positive_binary(self):
        self.binary_output.number = 2
        self.assertEqual(self.binary_output.binary_number, '0010')

    def test_negative_binary(self):
        self.binary_output.number = -2
        self.assertEqual(self.binary_output.binary_number, '1010')

    def test_float_input(self):
        self.binary_output.number = 2.5
        self.assertEqual(self.binary_output.binary_number, '0010')

    def test_negative_float_input(self):
        self.binary_output.number = -2.5
        self.assertEqual(self.binary_output.binary_number, '1010')

    def test_not_all_numeric_str(self):
        self.binary_output.number = '-test-str2ing'
        self.assertEqual(self.binary_output.binary_number, '1010')

    def test_only_minus_sign(self):
        self.binary_output.number = '---'
        self.assertIsNone(self.binary_output.binary_number)

    def test_only_float_points(self):
        self.binary_output.number = '...'
        self.assertIsNone(self.binary_output.binary_number)

    def test_only_text(self):
        self.binary_output.number = 'test_string'
        self.assertIsNone(self.binary_output.binary_number)


unittest.main()
