string="lost soul"
print(string)
#join method
s='statistic'
m='MATHEMATICS'
print("*".join(m))
print(s.join(m))

items=["apple","banana","cherry"]
result="@@".join(items)
print(result)

word=("python","is","fun")
result1="--".join(word)
print(result1)

#split method
a="Akshada"
print(a.split())
print(a.split("a"))

#split the string
s=("python is the language")
print(s.split())
#return true for capital letter
print(s.isupper())
#return true for small letter
print(s.islower())
#return true all are digit
print(s.isdigit())
#when there is white space then it return true
b=" "
print(b.isspace())