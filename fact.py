num=int(input("Enter the number :"))
factorial=1
if num==0:
    print("The factorail of the zero is one")
elif num<0:
    print("Negative number have not factorial")
else:
    for i in range(1,num+1):
        factorial=factorial*(i)
print("The factorial of the given num is",factorial)
