#28.Write a Python program to implement the merge sort algorithm
def merge_sort(arr):
   
    if len(arr) > 1:
        
        mid = len(arr) // 2

        
        left_half = arr[:mid]
        right_half = arr[mid:]

       
        merge_sort(left_half)
        merge_sort(right_half)

       
        i = j = k = 0

        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1


        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


if __name__ == "__main__":
    test_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", test_array)
    merge_sort(test_array)
    print("Sorted array:", test_array)

        