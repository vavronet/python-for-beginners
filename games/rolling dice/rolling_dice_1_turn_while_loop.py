import random 

game_end = False

print('Welcome to the rolling dice game!')
input('Press enter to continue')

while game_end == False:
    user_dice_1 = random.randint(1,6)
    user_dice_2 = random.randint(1,6)
    computer_dice_1 = random.randint(1,6)
    computer_dice_2 = random.randint(1,6)
    print('Your dice numbers are {} and {}!'.format(user_dice_1, user_dice_2))
    print('The computer dice numbers are {} and {}!'.format(computer_dice_1, computer_dice_2))

    if user_dice_1 + user_dice_2 > computer_dice_1 + computer_dice_2:
        print('YOU WON, YOu mad lad!!')
    elif user_dice_1 + user_dice_2 < computer_dice_1 + computer_dice_2:
        print('NO! You fool! What have you done! You have lost, you madlad!')
    else:
        print('Well, thats a twist. Its a tie.')
    
    if input('Do you wish to continue? Y/N\n') == 'N':
        game_end = True
        print('Goodbye!')