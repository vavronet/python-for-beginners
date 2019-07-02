import list_of_words
import game_functions

# initialize variables
tries_left = 8
guessed_letters = []
wrong_letters = []
letter = ''

# start game 
input('Welcome to our Hangman Game! Press enter to continue.\n')
print('You will have {} tries to get all the letters correct.'.format(tries_left))
input('Press enter to start the game!\n')

the_word = game_functions.get_random_element(list_of_words.hangman_list)
print(game_functions.show_placeholders(the_word, letter, guessed_letters))

input('Guess a letter and press enter!\n')
