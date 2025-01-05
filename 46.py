#6.Write a program that accepts 2 lists of 5 elements each and checks whether both lists have the same values/entries
#For ex: [1,3,5] and [3,5,1]
def check_lists_equal(list1, list2):
    
    return sorted(list1) == sorted(list2)


list1 = list(map(int, input("Enter 5 elements for the first list (space separated): ").split()))
list2 = list(map(int, input("Enter 5 elements for the second list (space separated): ").split()))

if check_lists_equal(list1, list2):
    print("Both lists have the same values.")
else:
    print("Both lists do not have the same values.")

