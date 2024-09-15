def sorted_words(string):
    word=string.split()
    word.sort()
    sorted_string='  '.join(word)
    return sorted_string
string="lazy fox climb on tree"
sorted_string=sorted_words(string)
print(sorted_string)
