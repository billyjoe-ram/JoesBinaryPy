from binary_from_int import BinaryFromInt

print("""
    Welcome to Joe's Binary Py! A simple, easy to use and tested application,
    to provide you fast output in any occasion you need! Type 'quit' when
    asked input or Ctrl + C to stop the application  
""")

# Recursion
while True:
    # Receives the input
    integer_input = input("Please, type an integer number: ")

    if type(integer_input) is str:
        if integer_input == 'quit':
            print('\nBye Bye! :)')
            break

    binary_number = BinaryFromInt(integer_input)

    if not binary_number.number() and not binary_number.binary_number():
        print('Invalid input!')
        continue

    print(f"The number you asked for ({binary_number.number()}) in binary is: {binary_number.binary_number()}")
