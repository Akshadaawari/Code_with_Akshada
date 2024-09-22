Num1=int(input("Enter the first Number :"))
Num2=int(input("Enter the second Number :"))

print(Num1,Num2)
if Num1>Num2:
    x=Num1
else:
    x=Num2
for i in range(1,x+1):
    if Num1%i==0 and Num2%i==0:
        gcd=i
print("the gcd is",gcd)
        