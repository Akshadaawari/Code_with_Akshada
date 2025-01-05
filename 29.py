#29.Write a Python function to remove all occurrences of a specific element from a list.
def remove_occurrences(lst, element):
    
    return [x for x in lst if x != element]
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 2, 5, 2, 6]
    element_to_remove = 2
    updated_list = remove_occurrences(original_list, element_to_remove)
    print("Original list:", original_list)
    print("Element to remove:", element_to_remove)
    print("Updated list:", updated_list)


