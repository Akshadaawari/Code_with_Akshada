#27.Write a Python program that counts the occurrences of each character in a string.
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] += 1
    else:
            char_count[char] = 1

    return char_count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = count_characters(user_input)
    print("Character occurrences:")
    for char, count in result.items():
        print(f"'{char}': {count}")
