# Create a 2D list (matrix) of 3 rows and 3 columns. Write a program to display the matrix and calculate the sum of all diagonal elements. 

# 2D matrix 
matrix=[
    [1, 2, 3],    # this is first row 
    [4, 7, 6],    # this is second row 
    [7, 8, 13]     # this is third row 
]

for row in matrix:
    print(row)  # print all matrix 

# sum of diagonal elements
     # first diagonal elements is: 1, 7, 13
first_diagonal = sum(matrix[i][i] for i in range(3))
print("The sum of first diagnoal elements:", first_diagonal)

       # second diagonal elements is: 3,7,7
second_diagonal = sum(matrix[i][2-i] for i in range(3))
print("The sum of first diagnoal elements:", second_diagonal)

# Sum of two diagonal elements
Sum = first_diagonal + second_diagonal
print("The sum of two diagnoal elements is :", Sum )