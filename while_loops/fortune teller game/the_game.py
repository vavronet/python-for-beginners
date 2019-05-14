import fortunes_list
import random

#TODO 1: validation for user input other than Y or N
#TODO 2: fix program to not show line 8 twice 

exit_game = False
print('Welcome to Fortune Teller Simulator.')
print(fortunes_list.the_list[random.randint(0, len(fortunes_list.the_list)-1)])

while exit_game == False:
    print(fortunes_list.the_list[random.randint(0, len(fortunes_list.the_list)-1)])
    user_input = input('Do you wish for another fortune? (Y/N)\n')
    if user_input == 'N':
        exit_game = True
        print('bYe oLd fRiEnD!')