import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

def countConnectedComponent(v):
    visited[v] = 1
    for i in range(1, n+1):
        if (matrix[v][i] and (not visited[i])):
            countConnectedComponent(i)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u][v] = matrix[v][u] = 1

cnt = 0
for v in range(1, n+1):
    if not visited[v]:
        if (1 not in matrix[v]):     # 정점에 연결된 간선이 없는 경우
            cnt += 1
            visited[v] = 1
        else:
            countConnectedComponent(v)
            cnt += 1

print(cnt)