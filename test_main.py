import unittest

from binary_from_int import BinaryFromInt


class TestBinaryPy(unittest.TestCase):
    def test_class(self):
        binary_output = BinaryFromInt(2)
        self.assertIsNotNone(binary_output.number())

    def test_numeric(self):
        binary_output = BinaryFromInt('3.5')
        self.assertIsInstance(binary_output.number(), int)

    def test_not_float(self):
        binary_output = BinaryFromInt(3.5)
        self.assertNotIsInstance(binary_output.number(), float)

    def test_positive_binary(self):
        binary_output = BinaryFromInt(2)
        self.assertEqual(binary_output.binary_number(), '0010')

    def test_negative_binary(self):
        binary_output = BinaryFromInt(-2)
        self.assertEqual(binary_output.binary_number(), '1010')


unittest.main()
