#37.Given an array of strings, group anagrams together.
#(An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once)
#Example:
#Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#Output: [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']]
from collections import defaultdict

def group_anagrams(strings):
    anagrams = defaultdict(list)  
    for word in strings:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
        return list(anagrams.values())
input_strings = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
output = group_anagrams(input_strings)
print("Grouped Anagrams:", output)
