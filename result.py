name=input("Emter your good name :")
roll_no=int(input("Enter your roll no :"))

#for i in range(0,100):
English=int(input("Enter the English marks (0-100) :"))
Maths=int(input("Enter the Maths marks (0-100) :"))
Hindi=int(input("Enter the hindi marks(0-100)"))
social_science=float(input("Enter the Social science marks (0-100) :"))
science=float(input("Enter the Science marks (0-100) :"))
if 0<=English<=100:
    print(English)
elif 0<=Maths<=100:
    print(Maths)
elif 0<=Hindi<=100:
    print(Hindi)
elif 0<=social_science<=100:
    print(social_science)
elif 0<=science<=100:
    print(science)
else:
    print("Enter Valid Marks")

print(str(name))
print(int(roll_no))   
avg=(English+Maths+Hindi+science+social_science)/5
percentage=avg*100
print("Your percentage is",percentage)
if percentage>36:
    print("Congratulation you are passed")
else:
    print("Better luck next time")



