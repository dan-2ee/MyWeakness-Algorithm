import sys

def isValid(word):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    if not any(char in vowels for char in word):
        return False 
    for i in range(len(word)-2):
        if all(char in vowels for char in word[i:i+3]):
            return False
        if all(char in consonants for char in word[i:i+3]):
            return False
    for i in range(len(word)-1):
        if (word[i] != "e" and word[i] != "o" and word[i] == word[i+1]):
            return False
    return True

input = sys.stdin.readline

while (1):
    word = input().strip()
    if (word == "end"): break
    print("<{}> is acceptable.".format(word)) if (isValid(word)) else print("<{}> is not acceptable.".format(word))
        
