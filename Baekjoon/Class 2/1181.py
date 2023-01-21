import sys

N = int(sys.stdin.readline())
wordLst = list(set(sys.stdin.readline().strip() for _ in range(N)))
wordLst.sort(key=lambda x: (len(x), x))

for word in wordLst:
    print(word)
