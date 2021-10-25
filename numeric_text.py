from filter_alnum import filter_alnum


class NumericText:
    def __init__(self, number_value):
        self._number = number_value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, int_number):
        int_number = filter_alnum(int_number)
        if int_number:
            self._number = int(float(int_number))
        else:
            self._number = None

    def is_negative(self):
        return self.number < 0

    def is_float(self):
        return type(self.number) is float

    def is_integer(self):
        return type(self.number) is int
