#26.Write a Python function to find the sum of all even numbers in a list.
def cal(numbers):
    even_sum = sum(i for i in numbers if i % 2 == 0)
    return even_sum

l1 = [1, 2, 3, 4, 5, 6]
print(cal(l1))