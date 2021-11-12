import unittest
from binary_from_int import BinaryNumericText


class TestBinaryPyCalc(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.binary_first = BinaryNumericText()
        cls.binary_second = BinaryNumericText()

    def test_result_four(self):
        self.binary_first.number = 2
        self.binary_second.number = 2
        sum_result = self.binary_first.add(self.binary_second)
        self.assertEqual(sum_result, '0100')

    def test_result_ten(self):
        self.binary_first.number = 5
        self.binary_second.number = 5
        sum_result = self.binary_first.add(self.binary_second)
        self.assertEqual(sum_result, '01010')

    def test_result_twenty(self):
        self.binary_first.number = 15
        self.binary_second.number = 5
        sum_result = self.binary_first.add(self.binary_second)
        self.assertEqual(sum_result, '010100')

    def test_result_thirty(self):
        self.binary_first.number = 15
        self.binary_second.number = 15
        sum_result = self.binary_first.add(self.binary_second)
        self.assertEqual(sum_result, '011110')


unittest.main()
