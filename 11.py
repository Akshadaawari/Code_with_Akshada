#Write a Python function to find the second largest number in a list.
def sec_max(n):
    x=max(n)
    n.remove(x)
    z=max(n)
    return z
list=[1,2,3,4,5,6,7]
print("The second largest element in list is",sec_max(list))


