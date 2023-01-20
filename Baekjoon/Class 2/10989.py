import sys

N = int(sys.stdin.readline())
numCount = [0 for _ in range(10001)]

for _ in range(N):
    numCount[int(sys.stdin.readline())] += 1

for i in range(10001):
    if (numCount[i]):
        for j in range(numCount[i]):
            print(i)
