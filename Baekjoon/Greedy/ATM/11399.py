import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()

result = 0
for i in range(n):
    result += sum(times[:i+1])

print(result)