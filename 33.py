#3.Write a program that takes a number N as input from the user and prints pascal’s triangle of N height/steps.
#Pascal's triangle is a triangular array constructed by summing adjacent elements in preceding rows.
#For example if N = 4 """ 1 1 1 1 2 1 1 3 3 1 """ 34.Write a program to reverse a stack using recursion.

def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)))


N = int(input("Enter the number of levels for Pascal's Triangle: "))
pascals_triangle(N)
