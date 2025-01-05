#Write a Python function to count the number of vowels in a string
#(def my_function(*kids):
 #   print("The youngest child is   " +kids[2])
#my_function("Akshada","Awari","Vishwajeet")
vowel="aeiouAEIOU"
def vow(n):
    count=0
    for char in str:
        if char in vowel:
            count +=1
    return count
str="Akshada Awari"
a=vow(str)
print(a)
    


