import random 
import english_disctionary_rolling_dice
import romanian_disctionary_rolling_dice

game_end = False
user_sum = 0
computer_sum = 0

print('Welcome to the rolling dice game!')

language_is_selected = False
language_dictionary = english_disctionary_rolling_dice.rolling_dice_english

while language_is_selected == False:
    language = input('Please select the language: e/English, r/Romanian \n')
    if language == 'e':
        language_is_selected = True
        print('You selected English.')
    elif language == 'r':
        language_is_selected = True
        language_dictionary = romanian_disctionary_rolling_dice.rolling_dice_romanian
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
    input(language_dictionary['continue'])

while game_end == False:
    user_dice_1 = random.randint(1,6)
    user_dice_2 = random.randint(1,6)
    computer_dice_1 = random.randint(1,6)
    computer_dice_2 = random.randint(1,6)
    user_sum = user_dice_1 + user_dice_2 + user_sum
    computer_sum = computer_dice_1 + computer_dice_2 + computer_sum
    print(language_dictionary['person_dice'].format(user_dice_1, user_dice_2, user_sum))
    print(language_dictionary['computer_dice'].format(computer_dice_1, computer_dice_2, computer_sum))
    
    if user_sum > target or computer_sum > target:
        game_end = True
    else:
        input(language_dictionary['continue'])
else:
    if user_sum > computer_sum:
        print(language_dictionary['win'])
    elif user_sum < computer_sum:
        print(language_dictionary['loose'])
    else:
        print(language_dictionary['tie'])