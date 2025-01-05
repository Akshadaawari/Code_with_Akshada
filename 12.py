#12.Write a program to print Fibonacci sequence up to n numbers.
def Fibo(n):
    if n<0:
        print("invalid")
    elif n==1 or n==1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
num=int(input("Enter the number :"))   
print(Fibo(num))