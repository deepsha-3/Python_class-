
# Creating A using a loop

# num = 8
# for i in range(num):
#     if i == 0:
#         print(' ' * (num - i - 1) + '*' + ' ' * (num - i - 1))
#     elif i == num // 2:
#         print('*' * (2 * num - 1))
#     else:
#         print(' ' * (num - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

n= 5
for i in range(n,-1,-1):                      
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(i+1):
        print("*",end=" ")
    print()
  