#23.Write a Python function to count the number of words in a string.
def cal(str):
    words=str.split()
    return len(words)
string=input("Enter the string")
print("The total count of words in string :",cal(string))