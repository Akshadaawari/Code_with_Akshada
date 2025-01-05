#35.Write a Python function to find the longest substring without repeating characters.
def longest_unique_substring(s):
    start = 0 
    max_length = 0  
    max_substring = "" 
    char_index = {}  

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
          
            start = char_index[s[end]] + 1

        
        char_index[s[end]] = end

        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end + 1]

    return max_substring, max_length


input_string = input("Enter a string: ")
substring, length = longest_unique_substring(input_string)
print(f"Longest substring without repeating characters: '{substring}' with length {length}")
