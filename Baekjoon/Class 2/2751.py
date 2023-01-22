import sys

N = int(sys.stdin.readline())
words = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(words):
    print(i)
