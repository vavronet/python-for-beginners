import random 

game_end = False
user_sum = 0
computer_sum = 0

print('Welcome to the rolling dice game!')

rolling_dice_english = {
    'input_target': 'Please type in a number to set your target:\n',
    'integer_error': 'That is not an integer.'
}

rolling_dice_romanian = {
    'input_target': 'Te rog sa alegi un numar pentru scorul final:\n',
    'integer_error': 'Nu ai introdus un numar.'
}

language_is_selected = False
language_dictionary = rolling_dice_english

while language_is_selected == False:
    language = input('Please select the language: e/English, r/Romanian \n')
    if language == 'e':
        language_is_selected = True
        print('You selected English.')
    elif language == 'r':
        language_is_selected = True
        language_dictionary = rolling_dice_romanian
        print('Ai selectat limba Romana.')
    else:
        print('Invalid input.')

target_is_integer = False

while target_is_integer == False:
    try:
        target = int(input(language_dictionary['input_target']))
        target_is_integer = True
    except ValueError:
        print(language_dictionary['integer_error'])
else: 
    input('Press enter to continue')

while game_end == False:
    user_dice_1 = random.randint(1,6)
    user_dice_2 = random.randint(1,6)
    computer_dice_1 = random.randint(1,6)
    computer_dice_2 = random.randint(1,6)
    user_sum = user_dice_1 + user_dice_2 + user_sum
    computer_sum = computer_dice_1 + computer_dice_2 + computer_sum
    print('Your dice numbers are {} and {}! Your total is {}.'.format(user_dice_1, user_dice_2, user_sum))
    print('The computer dice numbers are {} and {} The computer total is {}!'.format(computer_dice_1, computer_dice_2, computer_sum))
    
    if user_sum > target or computer_sum > target:
        game_end = True
    else:
        input('Press enter to continue\n')
else:
    if user_sum > computer_sum:
        print('You won!')
    elif user_sum < computer_sum:
        print('Computer won, you madlad!')
    else:
        print('There has been a tie!')