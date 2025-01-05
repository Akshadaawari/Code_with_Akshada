#9.Write a Python function that returns the factorial of a number.
num=int(input("Enter the number"))
def fact(n):
    if n==0 or n==1:
       return 1
       
    else:
       return n * fact(n-1)
    
            
print(fact(num))