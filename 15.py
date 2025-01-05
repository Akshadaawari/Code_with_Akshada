#15.Write a Python  function to find the smallest number in a list.
list=[19,12,13,14,15]
def small(n):
    smallest=n[0]
    for i in n:
        if i < smallest:
            smallest=i
    return smallest
print(small(list))