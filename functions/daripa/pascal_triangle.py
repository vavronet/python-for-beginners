# Create a function that prints on the screen the Pascal triangle with n rows.
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1 

def pascal_triangle(n):
    last = []
    row = 1
    while row <= n:
        content = [1]
        if row == 1:
            continue
        elif row == 2:
            content.append(1)
        else:
            unknown = 1
            while unknown <= row - 2:
                content.append(1)
                unknown = unknown + 1
            content.append(1)
        print(content)
        last = content
        row = row + 1 

pascal_triangle(9)