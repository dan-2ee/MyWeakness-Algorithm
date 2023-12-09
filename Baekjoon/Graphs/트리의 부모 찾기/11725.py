import sys

sys.setrecursionlimit(10**6)
def dfs(parent):
    for v in matrix[parent]:
        if not visited[v]:
            visited[v] = parent
            dfs(v)

input = sys.stdin.readline
N = int(input())
matrix = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited[1] = 1

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)

dfs(1)
for i in visited[2:]:
    print(i)
