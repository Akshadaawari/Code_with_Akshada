#.Write a program to check if a string is a palindrome.
str=input("Enter the string  :")
if str==str[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
