def capture_integer_from_input(input_text):
    is_integer = False

    while is_integer == False:
        try:
            user_number = int(input(input_text))
            is_integer = True
        except ValueError:
            print('Error. You have to type in an integer.')
    else:
        return user_number

captured_integer = capture_integer_from_input('Please enter your age:\n')

print(captured_integer)