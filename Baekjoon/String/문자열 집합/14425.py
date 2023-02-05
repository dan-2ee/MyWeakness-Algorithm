import sys

n, m = map(int, sys.stdin.readline().split())
nSet = set(sys.stdin.readline().strip() for _ in range(n))
cnt = 0
for _ in range(m):
    item  = sys.stdin.readline().strip()
    if item in nSet:
        cnt += 1

print(cnt)