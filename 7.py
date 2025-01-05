num=int(input("Enter the number :"))
if num==1 or num==0:
    print("num is not prime")
flag=1
for i in range(2,num):
    if num%i==0:
        flag=0
        break
if flag==1:
    print("number is prime")
else:
    print("number is not prime")