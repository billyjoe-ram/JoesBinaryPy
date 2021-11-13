from binary_from_int import BinaryNumericText

print("""
Welcome to Joe's BinaryNumericText Py! A simple, easy to use and tested application,
to provide you fast output in any occasion you need!""")


def main():
    print("""
1 - Convert number
2 - Sum numbers
3 - Quit
\n""")
    module = pick_module()
    if module != 'Quit':
        if module == 'Convert':
            convert_number()
        else:
            add_binaries()
    else:
        print('\nBye Bye! :)')


def convert_number():
    keep_converting = True
    while keep_converting:
        integer_input = input("Please, type an integer number: ")

        binary_number = BinaryNumericText()
        binary_number.number = integer_input

        if type(integer_input) is str:
            if not binary_number.number and not binary_number.binary_number:
                print('Invalid input!')
            else:
                print(f"The number you asked for ({binary_number.number}) in binary is: {binary_number.binary_number}")
        keep = input('\nKeep converting numbers? Y / N ')
        if keep.upper().strip() == 'N':
            keep_converting = False
    main()


def handle_input():
    allowed_options = ['1', '2', '3']
    user_option = input('Choose a module or quit: ').strip()

    if user_option in allowed_options:
        return user_option
    else:
        print('Invalid input! Pick again')
        handle_input()


def pick_module():
    module_number = handle_input()
    if module_number == '1':
        module_name = 'Convert'
    elif module_number == '2':
        module_name = 'Sum'
    else:
        module_name = 'Quit'

    return module_name


def add_binaries():
    keep_adding = True
    while keep_adding:
        first_number = int(input('Please, type an integer number: '))
        second_number = int(input('Please, type a second integer number: '))

        first_binary = BinaryNumericText(first_number)
        second_binary = BinaryNumericText(second_number)

        if first_binary.is_negative() or second_binary.is_negative():
            print('Please, only positive numbers in this sum')
            pass

        if first_binary.is_float() or second_binary.is_negative():
            print('Please, only integers numbers in this sum')
            pass

        print(f'{first_number} in binary is {first_binary.binary_number}')
        print(f'{second_number} in binary is {second_binary.binary_number}')

        print('Adding...')

        # Waiting without using time.sleep()
        for i in range(500):
            i += i

        result = first_binary.add(second_binary)

        print(f'The result in binary is {result}')

        keep = input('\nKeep adding numbers? Y / N ')
        if keep.upper().strip() == 'N':
            keep_adding = False
    main()


main()
