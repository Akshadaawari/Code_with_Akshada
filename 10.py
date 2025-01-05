#10.Write a Python function to find the length of a string without using len()
s="abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def cal_len(str):
    count=0
    for char in str:
        if char in str:
            count +=1 
    return count
new_str=input("Enter the string :")
print(cal_len(new_str))