def swar_count(string):
    vowel=set("aeiouAEIOU")
    count=0
    for alphabet in string:
        if alphabet in vowel:
            count +=1
    return count
string="Go and get a job first"
result=swar_count(string)
print("number of vowels in givent string",result)