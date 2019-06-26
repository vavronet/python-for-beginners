# Create a function that retrieves a random element from a list of strings and displays on the screen an underscore character for each letter.
import random

def get_random_element(a_list):
    random_index = random.randint(0,len(a_list)-1)
    random_element = a_list[random_index]
    return random_element

def show_placeholders(word, letter, guessed_letters):
    word_capitals = word.upper()
    letter_capital = letter.upper()
    placeholders = ''
    for x in word_capitals:
        if x == letter_capital:
            placeholders = placeholders + x + ' '
            guessed_letters.append(letter_capital)
        elif (x in guessed_letters) == True:
             placeholders = placeholders + x + ' '
        else:
            placeholders = placeholders + '_ '
    return placeholders

b_list = ['Lorem', 'ipsum', 'dolor', 'amet', 'consectetur', 'adipiscing', 'elit', 'eiusmod', 'tempor', 'incididunt', 'labore', 'et', 'dolore', 'magna', 'aliqua']

the_word = get_random_element(b_list)
guessed = ['A', 'I']

print(guessed)
print(the_word)
print(show_placeholders(the_word, 'o', guessed))
print(guessed)
