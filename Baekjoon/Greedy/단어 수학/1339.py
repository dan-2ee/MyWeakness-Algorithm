import sys

input = sys.stdin.readline
N = int(input())
words = [input().strip() for _ in range(N)]

alphabet = {}
for word in words:
    l = len(word)
    for idx, char in enumerate(word):
        if char in alphabet:
            alphabet[char] += (10 ** (l-idx-1))
        else:
            alphabet[char] = (10 ** (l-idx-1))

sum = 0
alphabetCounts = dict(sorted(alphabet.items(), key=lambda x:x[1], reverse=True))
for idx, alphabet in enumerate(alphabetCounts.values()):
    sum += (alphabet * (9-idx))

print(sum)