# Return a random element from a list.
import random

def get_random_element(a_list):
    random_index = random.randint(0,len(a_list)-1)
    random_element = a_list[random_index]
    return random_element

b_list = ['Lorem', 'ipsum', 'dolor', 'amet', 'consectetur', 'adipiscing', 'elit', 'eiusmod', 'tempor', 'incididunt', 'labore', 'et', 'dolore', 'magna', 'aliqua']

print(get_random_element(b_list))