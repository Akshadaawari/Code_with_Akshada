#20.Write a program to find the common elements between two lists.
def common_element(l1,l2):
    return list(set(l1)&set(l2))
list1=[1,2,3,4]
list2=[3,4,2]
same_element=common_element(list1,list2)
print("THe common element between two list :",same_element)