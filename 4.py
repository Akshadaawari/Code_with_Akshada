#.Write a Python function to check if a number is even or odd
def even_odd(n):
    if n%2==0:
         return "Number is Even"
    else:
         return "Number is odd"
l=int(input("Enter the number :"))
z=even_odd(l)
print(z)


