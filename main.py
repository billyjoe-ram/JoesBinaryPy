from binary_from_int import BinaryNumericText

print("""
    Welcome to Joe's BinaryNumericText Py! A simple, easy to use and tested application,
    to provide you fast output in any occasion you need! Type 'quit' when
    asked input to stop the application  
""")


def main():
    integer_input = input("Please, type an integer number: ")

    binary_number = BinaryNumericText()
    binary_number.number = integer_input

    if type(integer_input) is str:
        if integer_input == 'quit':
            print('\nBye Bye! :)')
        else:
            if not binary_number.number and not binary_number.binary_number:
                print('Invalid input!')
            else:
                print(f"The number you asked for ({binary_number.number}) in binary is: {binary_number.binary_number}")
            main()


main()
