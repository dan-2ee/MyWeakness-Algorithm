import sys

word = sys.stdin.readline().strip().lower()
wordSet = list(set(word))
wordCnt = []

for i in wordSet:
    wordCnt.append(word.count(i))

if (wordCnt.count(max(wordCnt)) >= 2):
    print("?")
else:
    print(wordSet[wordCnt.index(max(wordCnt))].upper())
