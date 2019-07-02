import random

# Returns a random element from a given list 
def get_random_element(a_list):
    random_index = random.randint(0,len(a_list)-1)
    random_element = a_list[random_index]
    return random_element

# Returns the formatted word with underscores for the unguessed letters 
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