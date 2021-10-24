from filter_alnum import filter_alnum


class BinaryNumber:
    """
        Class created to convert integer to binary number
    """
    def __init__(self, int_number=None):
        self.int_number = int_number

    @property
    def number(self):
        return self.int_number

    @number.setter
    def number(self, int_number):
        int_number = filter_alnum(int_number)
        if int_number:
            self.int_number = int(float(int_number))
        else:
            self.int_number = None

    @property
    def binary_number(self):
        return self.parse_integer_to_bin()

    def parse_integer_to_bin(self):
        """
            Receives a numeric string as input and returns a string equivalent
            to that number in a binary base.
        """
        if not self.number:
            return self.number

        integer_number = self.number * -1 if self.most_significant_bit() else self.number
        # Empty string to concat the binary
        binary_string = ""

        # Iterates while division is possible
        while integer_number >= 1:
            # Gets the rest
            binary_string += str(integer_number % 2)
            # Gets the integer part after division
            integer_number = int(integer_number / 2)

        # If is negative, adds the more significant bit to represent
        # negative
        if self.most_significant_bit():
            binary_string += '1'
        else:
            binary_string += '0'

        # and parses it to string again
        binary_string = binary_string[::-1]

        return binary_string

    def most_significant_bit(self):
        if self.number < 0:
            return True
        return False

    def check_bits_needed(self):
        """
        For the constructed class, returns the number
        of bits needed to represent the number (8, 16,
        32...)
        :return: bits_needed
        :rtype: int
        """
        bits_needed = 1

        while abs(self.number) >= (2 ** bits_needed):
            bits_needed += 1

        if self.most_significant_bit():
            bits_needed += 1

        return bits_needed
