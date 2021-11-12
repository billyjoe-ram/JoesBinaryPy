class BitComparator:
    """
    Compares two bits using boolean algebra
    """

    @staticmethod
    def compare_bits_xor(first_bit, second_bit):
        """
        Applies an 'xor' (exclusive or) boolean operation for the
        given two bits
        :param first_bit:
        :type first_bit: int
        :param second_bit:
        :type second_bit: int
        :return: xor_result
        :rtype: bool
        """
        return first_bit ^ second_bit

    @staticmethod
    def compare_bits_and(first_bit, second_bit):
        """
        Applies an 'and' boolean operation for the
        given two bits
        :param first_bit:
        :type first_bit: int
        :param second_bit:
        :type second_bit: int
        :return: and_result
        :rtype: bool
        """
        return first_bit and second_bit
