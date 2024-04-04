import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M = map(int, input().split())
matrix = [[0] for _ in range(N+1)]

def dfs(node):
    visited[node] = 1
    for n in matrix[node][1:]:
        if not visited[n]:
            dfs(n)
        
for _ in range(M):
    v1, v2 = map(int, input().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)

visited = [0]*(N+1)
group = 0
for v in range(1,N+1):
    if not visited[v] and matrix[v] == [0]:
        group += 1  # 연결 요소가 없는 경우 
    elif not visited[v]:  # 연결 요소가 있는 경우 
        dfs(v)
        group += 1
print(group)