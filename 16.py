#16.Write a Python function to convert a string to uppercase without using upper().
def to_uppercase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    
    return result

input_string = input("Enter a string: ")
uppercase_string = to_uppercase(input_string)
print("String in uppercase:", uppercase_string)


    