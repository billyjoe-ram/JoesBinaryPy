from filter_alnum import filter_alnum


class NumericText:
    def __init__(self, number_value):
        self.__number = number_value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, int_number):
        int_number = filter_alnum(int_number)
        if int_number:
            self.__number = int(float(int_number))
        else:
            self.__number = None

    @property
    def absolute_number(self):
        return abs(self.number)

    def is_negative(self):
        return self.number < 0

    def is_float(self):
        return type(self.number) is float

    def is_integer(self):
        return type(self.number) is int
