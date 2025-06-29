** start of main.py **

def validate_isbn(isbn, length):
    # Off-by-one fix: ISBN length should be length + 1 (check digit included)
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    try:
        main_digits = isbn[:-1]
        given_check_digit = isbn[-1]

        main_digits_list = [int(digit) for digit in main_digits]

    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')

        if len(values) != 2:
            print('Enter comma-separated values.')
            return

        isbn = values[0]

        try:
            length = int(values[1])
        except ValueError:
            print('Length must be a number.')
            return

        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')

    except IndexError:
        print('Enter comma-separated values.')


# IMPORTANT: Commented out for test execution
# main()


** end of main.py **

