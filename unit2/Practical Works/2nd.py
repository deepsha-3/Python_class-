# Write program to utilize different loop statements to solve meaningful problems.

# 1. For loop to print even numbers from 0 to 20 
print("For loop to print even numbers from 0 to 20:")
for i in range (0, 21):
    if i % 2 == 0:
        print(i)
print("")



# 2. While loop to calculate the sum of numbers from 1 to 100
print("While loop to calculate the sum of numbers from 1 to 100:")

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print("Sum is:", sum)