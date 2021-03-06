import unittest
from binary_from_int import BinaryNumericText


class TestBitsInNumber(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.binary_output = BinaryNumericText()

    def test_class(self):
        self.binary_output.number = 2
        self.assertIsNotNone(self.binary_output.number)

    def test_min_bits_positive(self):
        self.binary_output.number = 64
        self.assertEqual(self.binary_output.check_bits_needed(), 8)

    def test_min_bits_negative(self):
        self.binary_output.number = -64
        self.assertEqual(self.binary_output.check_bits_needed(), 8)

    def test_two_bit_representation(self):
        self.binary_output.number = 2
        self.assertEqual(self.binary_output.check_bits_needed(), 3)

    def test_four_bit_representation(self):
        self.binary_output.number = 8
        self.assertEqual(self.binary_output.check_bits_needed(), 5)

    def test_six_bit_representation(self):
        self.binary_output.number = 32
        self.assertEqual(self.binary_output.check_bits_needed(), 7)

    def test_bits_flipped(self):
        self.binary_output.number = 2
        self.assertEqual(self.binary_output.binary_bits_flipped(self.binary_output.binary_number), '101')


unittest.main()
