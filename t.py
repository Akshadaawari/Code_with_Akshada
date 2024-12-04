upper_count=0
lower_count=0
number_count=0
special_char_count=0


while True:
    p=input("Enter:")   # Python1$

    for i in p:
        if(i.isupper()):
            upper_count+=1
        if(i.islower()):
            lower_count+=1
        if(i.isnumeric()):
            number_count+=1
        if(i in ("$","_","%")):
            special_char_count+=1
        
    if(len (p)>=9 and upper_count>0 and lower_count>0 and number_count>0 and special_char_count>0):
        print("Success")
        break
    else:
        print("wrong")
        if len(p)<9:
            print("password must contain alteast p char")
        if upper_count==0:
            print("Password must contain Upper case ")
        if lower_count==0:
            print("Password must contain Lower case")
        if number_count==0:
            print("Password must contain Numeric case")
        if special_char_count==0:
            print("Password must contain Special case")
        print("Please try again")