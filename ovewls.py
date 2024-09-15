def vowel_count(str):
    vowel=set("aeiouAEIOU")
    count=0
    for aplphabet in str:
        if aplphabet in vowel:
            count +=1
    return count

str="Akshada"
result = vowel_count(str)
print("vowels in string",result)

    