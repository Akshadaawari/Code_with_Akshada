def factorial(n):
    if n==1 & n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter the Number  :"))
print("factorial of the",num,"is",factorial(num))


