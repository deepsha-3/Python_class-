
#   centered pyramid (isosceles triangle) 
num = 5
for i in range(num):
    spaces = num - i - 1
    stars = 2 * i + 1
    print(' ' * spaces + '*' * stars)
