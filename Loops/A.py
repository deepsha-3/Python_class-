
# Creating A using a loop

num = 8  # Even number

for i in range(num):
    if i == 0:
        # Top point
        print(' ' * (num - i - 1) + '*' + ' ' * (num - i - 1))
    elif i == num // 2 - 1:
        # Middle bar shifted up
        print('*' * (2 * num - 1))
    else:
        # Diagonal arms
        spaces_outside = num - i - 1
        spaces_inside = 2 * i - 1
        print(' ' * spaces_outside + '*' + ' ' * spaces_inside + '*')
