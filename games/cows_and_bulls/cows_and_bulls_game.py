import random

secret_number = random.randint(1000, 9999)
secret_string = str(secret_number)
number_of_tries = 0
typed_string = input('Type in a 4 digit number: \n')

def cows_and_bulls(secret, typed):
    print(secret)
    secret_list = []
    typed_list = []
    cows_list = []

    for x in secret:
        secret_list.append(x)

    for x in typed:
        typed_list.append(x)

    for x in typed_list:
        if x in secret_list:
            cows_list.append(x)

    cows = int(len(cows_list))    
    print(cows)

cows_and_bulls(secret_string, typed_string)