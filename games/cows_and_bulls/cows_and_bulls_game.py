import random

secret_number = random.randint(1000, 9999)
secret_string = str(secret_number)
number_of_tries = 0
typed_string = input('Type in a 4 digit number: \n')

def cows_and_bulls(secret, typed):
    print(secret)
    print(typed)
    print('3 cows, 2 bulls')


cows_and_bulls(secret_string, typed_string)