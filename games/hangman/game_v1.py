import list_of_words
import game_functions

# initialize variables
tries_left = 8
guessed_letters = []
wrong_letters = []
letter = ''
game_over = False 
placeholders = ''

# start game 
input('Welcome to our Hangman Game! Press enter to continue.\n')
print('You will have {} tries to get all the letters correct.'.format(tries_left))
input('Press enter to start the game!\n')

the_word = game_functions.get_random_element(list_of_words.hangman_list)
placeholders = game_functions.show_placeholders(the_word, letter, guessed_letters, wrong_letters)
print(placeholders)

while game_over == False:
    letter = input('Guess a letter and press enter!\n')
    letter = letter.upper()
    if letter in guessed_letters or letter in wrong_letters:
        print('You have already entered this letter.')
    else:
        placeholders = game_functions.show_placeholders(the_word, letter, guessed_letters, wrong_letters)
        print('\n' + placeholders + '\n')

        if letter in guessed_letters:
            print('You guessed a letter!')
        else:
            print('That letter is not in the word! Try again.')
            tries_left = tries_left - 1
        
        if tries_left == 0:
            print('Game over fam! This was your word:')
            print(the_word.upper())
            game_over = True
        else:
            if '_' in placeholders:
                print('You have {} tries left.\n'.format(tries_left))
            else:
                print('Great job fam you won!')
                game_over = True