num=int(input("Enter the number"))
x=1
print("Num")
if num<0:
    print("factorial is not exist")
elif num==0:
    print("factorial is 1")
else:
    for i in range (1,num+1):
        x=i*x
print("The factorai",num,"is",x)