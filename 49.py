#49.Write a Python function to count the number of occurrences of a word in a string.
def count_word_occurrences(string, word):
   
    words = string.split()  
    return words.count(word)  

string = input("Enter the string: ")
word = input("Enter the word to count occurrences: ")


count = count_word_occurrences(string, word)
print(f"The word '{word}' appears {count} time(s) in the given string.")
