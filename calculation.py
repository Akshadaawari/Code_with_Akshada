def add(x,y):
    return (x+y)
def substraction(x,y):
    return (x-y)
def multiplication(x,y):
    return (x*y)
def divide(x,y):
    return(x/y)
print("Select option")
print("1.Add")
print("2.substaction")
print("3.Multiplication")
print("4.dividation")
while True:
    choice=input("Enter the choice (1,2,3,4) :")
    if choice in ("1","2","3","4"):
        try:
            num1=float(input("Enter the first number"))
            num2=float(input("Enter the second number"))
        except ValueError:
            print("invalid input plz enter correct number")
            continue
        if choice =="1":
            print(num1,num2, "Addition is",add(num1,num2))
        elif choice =="2":
            print(num1,num2,"substraction is",substraction(num1,num2))
        elif choice =="3":
            print(num1,num2,"multiplication is",multiplication(num1,num2))
        elif choice =="4":
            print(num1,num2,"Dividation is",divide(num1,num2))
        nextCalculation=input("Enter yes/no ")
        if nextCalculation =="no":
         break
    else:
        print("invalid input")
