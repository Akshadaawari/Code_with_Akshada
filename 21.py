#21.Write a Python function to implement a basic calculator (+, -, *, /).
def cal(a,b,operator):
    if operator =="+":
        return a+b
    elif operator =="-":
        return a-b
    elif operator =="*":
        return a*b
    elif operator =="/":
        if b !=0:
            return a/b
        else:
            return "Error"
    else:
        return "invalid input"
num1=int(input("Enter the number first :"))
num2=int(input("Enter the second number :"))
calculation=cal(num1,num2,"+")
print(calculation)
     