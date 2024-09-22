def reverse(s):
    string=" "
    for i in s:
        string=i+string
    return string

s=input("enter your string  :")
print("your original string is i :",end=" ")
print(s)
print("your reverse string is :",end=" ")
print(reverse(s)) 


