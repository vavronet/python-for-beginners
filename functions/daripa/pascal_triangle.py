# Create a function that prints on the screen the Pascal triangle with n rows.
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1 
#1 5 10 10 5 1

def get_unknown_content(row, previous_row):
    unknown = []
    counter = 1
    while counter <= (row - 2):
        item = previous_row[counter] + previous_row[counter - 1]
        unknown.append(item)
        counter = counter + 1

    return unknown


def pascal_triangle(n):
    last_row = []
    row = 1
    while row <= n:
        content = [1]
       
        if row == 1:
            content = [1]
        elif row == 2:
            content.append(1)
        else:
            unknown = get_unknown_content(row, last_row)
            content = content + unknown
            content.append(1)
        
        print_row = ' '.join(map(str, content))
        spaces_before = ' ' * (n - row)
        print(spaces_before + print_row)
        last_row = content
        row = row + 1 

pascal_triangle(6)