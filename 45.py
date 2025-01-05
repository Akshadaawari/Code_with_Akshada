#PROBLEM STATEMENT
#Write a NumPy program to calculate the difference between
#  the maximum and the minimum values of a given array along the second axis
import numpy as np
arr = np.array([[3, 5, 7],
                [2, 8, 1],
                [4, 6, 9]])
max_values = np.max(arr, axis=1)
min_values = np.min(arr, axis=1)
difference = max_values - min_values
print("Array:")
print(arr)
print("\nDifference between maximum and minimum values along the second axis:")
print(difference)
