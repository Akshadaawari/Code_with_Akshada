#Write a Python function to find the intersection of two lists.
def find_intersection(list1, list2):

    intersection = []
    
   
    for item in list1:
       
        if item in list2 and item not in intersection:
            intersection.append(item)
    
    return intersection


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


result = find_intersection(list1, list2)
print("Intersection of the two lists:", result)
