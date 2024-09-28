def regular(x):
    return (90*x)
def silver(x):
    return (150*x)
def gold(x):
    return (200*x)
def platinum(x):
    return (300*x)
print("select choice")
print("1.regular_ticket")
print("2.silver_ticket")
print("3.gold_ticket")
print("4.platinum_ticket")
while True:
    choice=input("Enter the choice (1,2,3,4)  :")
    if choice  in ("1","2","3","4"):
        try:
            quantity=int(input("Enter the total quantity of the person"))
        except ValueError:
            print("Invalid choice plz enter the correct one")
            continue
        if choice =="1":
                print("the total prize of the movie ticket is",regular(quantity))
        elif choice =="2":
                print("the total prize of the movie ticket is",silver(quantity))
        elif choice =="3":
                print("the total price of the movie ticket is ",gold(quantity))
        elif choice =="4":
                print("the total price of the movie ticket",platinum(quantity))

        nextCalculation =input("yes,no")
        if nextCalculation ==" no":
         break
    else:
        print("invalid input")       




         


        