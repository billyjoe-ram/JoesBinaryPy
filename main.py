# Function to convert the number
def parse_integer_to_bin(integer_number):
    """
        Receives a numeric string as input and returns a string equivalent
        to that number in a binary base.
    """
    try:
        # Checks if user typed a float value (with floating point or comma)
        if ('.' or ',') in integer_number:
            raise ValueError
        else:
            integer_number = int(integer_number)

        # If is smaller than 0
        if integer_number < 0:
            raise ValueError

        # Empty string to concat the binary
        binary_string = ""

        # Iterates while division is possible
        while integer_number >= 1:
            # Gets the rest
            binary_string += str(integer_number % 2)
            # Gets the integer part after division
            integer_number = int(integer_number / 2)

        # and parses it to string again
        binary_string = binary_string[::-1]

        return binary_string
    except ValueError:
        print("Input must be an integer bigger or equal to 0")

    return False


# Control variable to prevent many many runs
times_ran = 0
run_limit = 50
# Recursion
while times_ran < run_limit:
    # Receives the input
    integer_input = input("Please, type an integer number: ")

    # Converts to binary
    number_parsed = parse_integer_to_bin(integer_input)

    # Outputs the conversion
    if number_parsed:
        times_ran += 1
        print(f"The number you asked for in binary is: {number_parsed}")
        print(f"Rounds left: {run_limit - times_ran}")
    else:
        print("Invalid input. Bye!")
        break
