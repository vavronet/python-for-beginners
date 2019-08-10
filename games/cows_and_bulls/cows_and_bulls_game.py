import random

secret_number = random.randint(1000, 9999)
secret_string = str(secret_number)
number_of_tries = 0
typed_string = input('Type in a 4 digit number: \n')

def cows_and_bulls(secret, typed):
    template = "{} cows, {} bulls"
    cows = 0
    bulls = 0
    idx = 0
    secret_at_idx = 0

    for x in typed:
        secret_at_idx = secret[idx]
        if x == secret_at_idx:
            cows = cows + 1
        elif x in secret:
            bulls = bulls + 1
        idx = idx + 1

    print(template.format(cows, bulls))

cows_and_bulls(secret_string, typed_string)

print(secret_string)

# 2 cows, 0 bulls
# idx = 0
# Secret String: 3962
# Typed String : 8342
# Step 1
# x = 8
# idx = 0
# secret_at_idx = secret[idx] = 3
# if x = secret_at_idx then add to cows (cows = cows + 1)
# elif x in secret then add to bulls (bulls = bulls + 1)
# idx = idx + 1
# Step 2
# x = 3
# idx = 1
# secret_at_idx = secret[idx] = 9
# if x = secret_at_idx then add to cows (cows = cows + 1)
# elif x in secret then add to bulls (bulls = bulls + 1)
# idx = idx + 1