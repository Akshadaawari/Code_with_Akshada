#38..Separate all lower case letters, 
# upper case letters ,special characters & numbers from
#  given string my_string=”ASdfesD@#HBDHB&^GUV%^*H45fdvnhw74w5e54uuU”
#Print the given string by the order of given below.
#1. Uppercases
#2. Lowercases
#3. Special Characters
#4. Numbers
def separate_characters(my_string):
    uppercases = []
    lowercases = []
    special_chars = []
    numbers = []

    for char in my_string:
        if char.isupper():
            uppercases.append(char)
        elif char.islower():
            lowercases.append(char)
        elif char.isdigit():
            numbers.append(char)
        else:
            special_chars.append(char)

    return ''.join(uppercases), ''.join(lowercases), ''.join(special_chars), ''.join(numbers)

my_string = "ASdfesD@#HBDHB&^GUV%^*H45fdvnhw74w5e54uuU"


uppercases, lowercases, special_chars, numbers = separate_characters(my_string)


print("Uppercases:", uppercases)
print("Lowercases:", lowercases)
print("Special Characters:", special_chars)
print("Numbers:", numbers)


print("Final String:", uppercases + lowercases + special_chars + numbers)
