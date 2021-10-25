from numeric_text import NumericText


class BinaryNumericText(NumericText):
    """
        Class created to convert integer to binary number
    """
    def __init__(self, int_number=None):
        super().__init__(int_number)

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

        integer_number = self.number * -1 if self.is_negative() else self.number
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
        if self.is_negative():
            binary_string += '1'
        else:
            binary_string += '0'

        # and parses it to string again
        binary_string = binary_string[::-1]

        return binary_string

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

        if self.is_negative():
            bits_needed += 1

        return bits_needed
