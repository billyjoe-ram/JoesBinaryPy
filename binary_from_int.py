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

    def binary_bits_flipped(self, binary_number=None):
        """
        Receives an the binary number in string as input and returns
        a string equivalent to that number with the bits flipped.
        If no number is passed, the value will be the "number" property
        :param binary_number:
        :type binary_number: str or None
        :return: complements_binary
        :rtype: str
        """
        if not binary_number:
            complements_binary = self.parse_integer_to_bin(self.absolute_number)
        else:
            complements_binary = binary_number

        complements_binary = complements_binary.replace('1', 'on')
        complements_binary = complements_binary.replace('0', 'off')

        complements_binary = complements_binary.replace('on', '0')
        complements_binary = complements_binary.replace('off', '1')

        return complements_binary

    def parse_integer_to_bin(self, number=None):
        """
        Receives an int numeric as input and returns a string equivalent
        to that number in a binary base. If no number is passed, the
        value will be the "number" property

        :param number:
        :type number: int
        :return: binary_string
        :rtype: str or None
        """
        if not self.number:
            return self.number

        if number is None:
            number = self.number

        integer_number = number * -1 if self.is_negative() else number
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

    def add(self, number_to_add=0):
        sum_result = self.number + number_to_add

        sum_result = self.parse_integer_to_bin(sum_result)

        return sum_result

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
