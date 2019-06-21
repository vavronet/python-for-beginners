# Create a function that will return the hightest number in a list.

def highest_number(some_list):
    great_number = some_list[0]
    for x in some_list:
        if x > great_number:
            great_number = x
    return great_number

some_list = [3, 6, 9, 1, 444, 8, 45, 87, 23, 98, 9,9, 22, 21, -5]
print(highest_number(some_list))