#25.Write a Python function that takes a number and returns the sum of its digits.
def sum(n):
    num=str(n)
    digit_sum = sum(int(digit) for digit in num)
    return digit_sum

number=45
print("THe sum of digit :",sum(number))