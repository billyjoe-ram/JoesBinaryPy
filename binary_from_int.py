from numeric_text import NumericText
from bit_comparator import BitComparator


class BinaryNumericText(NumericText):
    """
        Class created to convert integer to binary number
    """
    def __init__(self, int_number=None):
        super().__init__(int_number)
        self.__binary_number = ''
        self.__binary_flipped = ''

    @property
    def binary_number(self):
        return self.parse_integer_to_bin()

    @property
    def absolute_binary_number(self):
        absolute_binary = self.binary_number
        if self.is_negative():
            absolute_binary = list(absolute_binary)
            absolute_binary[0] = '0'
            absolute_binary = ''.join(absolute_binary)

        return absolute_binary

    @property
    def two_complements_representation(self):
        if self.is_negative():
            self.binary_bits_flipped(self.absolute_binary_number)

        return self.binary_number

    def parse_integer_to_bin(self):
        """
        Returns a string equivalent to the base 10
        number in the class attribute as a 2 base.

        :return: binary_string
        :rtype: str or None
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

        binary_string += self.most_significant_bit()

        # and parses it to string again
        binary_string = binary_string[::-1]

        return binary_string

    def add(self, binary_to_add):
        """
        Given a binary number represented in a string,
        sum it with the class defined binary and gives
        the result
        :param binary_to_add:
        :type binary_to_add: BinaryNumericText
        :return: result
        :rtype: result: str
        """
        result = ''
        carry_bit = 0

        if self.check_bits_needed() != binary_to_add.check_bits_needed():
            if self.check_bits_needed() > binary_to_add.check_bits_needed():
                binary_to_add = binary_to_add.extend_binary(self.check_bits_needed())
                first_binary = self.binary_number
            else:
                first_binary = self.extend_binary(binary_to_add.check_bits_needed())
                binary_to_add = binary_to_add.binary_number
        else:
            first_binary = self.binary_number
            binary_to_add = self.binary_number

        first_bin = first_binary[::-1]
        first_bin = [int(bit) for bit in first_bin]
        bin_to_add = binary_to_add[::-1]
        bin_to_add = [int(bit) for bit in bin_to_add]

        for i in range(len(first_bin)):
            resulting_bit = BitComparator.compare_bits_xor(first_bin[i], bin_to_add[i])

            if carry_bit:
                carry_bit = BitComparator.compare_bits_and(resulting_bit, carry_bit)
                resulting_bit = BitComparator.compare_bits_xor(resulting_bit, 1)
                if resulting_bit:
                    carry_bit = BitComparator.compare_bits_and(first_bin[i], bin_to_add[i])
            else:
                carry_bit = BitComparator.compare_bits_and(first_bin[i], bin_to_add[i])

            result += str(resulting_bit)

        result += self.most_significant_bit()

        result = result[::-1]

        return result

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

        # Bit for sign
        bits_needed += 1

        return bits_needed

    def extend_binary(self, bits_amount):
        """
        From the class binary_number (string),
        extend the number to be represented
        with more bits

        :return: extended_bits_binary
        :rtype: str
        """
        if bits_amount <= self.check_bits_needed():
            return self.binary_number

        bits_amount = bits_amount - self.check_bits_needed()

        extended_bits_binary = self.absolute_binary_number[:1]

        extended_bits_binary += '0' * bits_amount

        extended_bits_binary += self.absolute_binary_number[1:]

        return extended_bits_binary

    def most_significant_bit(self):
        """
            If is negative, adds the more significant bit to represent
            negative
            :return: most_significant_bit
            :rtype: str
        """
        if self.is_negative():
            return '1'
        return '0'

    @staticmethod
    def binary_bits_flipped(binary_string):
        """
        Returns a string equivalent to that number with the bits
        flipped.
        :return: complements_binary
        :rtype: str
        """
        # complements_binary = self.absolute_binary_number
        complements_binary = binary_string

        complements_binary = complements_binary.replace('1', 'on')
        complements_binary = complements_binary.replace('0', 'off')

        complements_binary = complements_binary.replace('on', '0')
        complements_binary = complements_binary.replace('off', '1')

        return complements_binary

    @staticmethod
    def compare_bits(first_bit, sec_bit, carry=False):
        """
        Compares to bits using boolean logic and returns
        the comparison. If asked for the carry (opt. param),
        it will return the carry bit in the comparison.

        :param first_bit:
        :type first_bit: int
        :param sec_bit:
        :type sec_bit: int
        :param carry:
        :type carry:
        :return: comparison or carry_bit
        :rtype:
        """
        comparison = 0
        carry_bit = 0
        # 1 xor 1
        # Results in 1 and no carry bit
        if first_bit ^ sec_bit:
            comparison = 1
            carry_bit = 0

        # 1 and 1
        # Results in 0 and a carry bit
        if first_bit and sec_bit:
            comparison = 0
            carry_bit = 1

        if not first_bit and not sec_bit:
            comparison = 0
            carry_bit = 0

        if carry:
            return carry_bit

        return comparison
