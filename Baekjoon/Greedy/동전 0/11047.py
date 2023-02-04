import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
idx = n-1   # 가장 큰 동전부터 탐색 
while(k):
    cnt += (k//coins[idx])
    k %= coins[idx]
    idx -= 1

print(cnt)

        