import random 

user_dice_1 = random.randint(1,6)
user_dice_2 = random.randint(1,6)
computer_dice_1 = random.randint(1,6)
computer_dice_2 = random.randint(1,6)

print('Welcome to the rolling dice game! *insert intro music* This lovely evening, you will be rolling two dice! But watch out, the computer is also rolling two dice! Whichever one of you has the highest sum will be the champion!! Good luck! ')
input('Press enter to continue.')
print('Your dice numbers are {} and {}!'.format(user_dice_1, user_dice_2))
print('The computer dice numbers are {} and {}!'.format(computer_dice_1, computer_dice_2))

if user_dice_1 + user_dice_2 > computer_dice_1 + computer_dice_2:
    print('YOU WON, YOu mad lad!!')
elif user_dice_1 + user_dice_2 < computer_dice_1 + computer_dice_2:
    print('NO! You fool! What have you done! You have lost, you madlad!')
else:
    print('Well, thats a twist. Its a tie.')
    
