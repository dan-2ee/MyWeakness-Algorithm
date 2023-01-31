import sys
from collections import deque

# 깊이 우선 탐색은 보통 재귀로 구현
# 너비 우선 탐색은 보통 큐나 데크 이용 
n, m, v = map(int, sys.stdin.readline().split())
# 인접 행렬 생성 (인덱스 0은 사용하지 않음)
matrix = [[0]*(n+1) for _ in range(n+1)]
# 방문한 정점 체크
visitedDfs = [0] * (n+1)
visitedBfs = [0] * (n+1)

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    matrix[n1][n2] = matrix[n2][n1] = 1

def dfs(v):    # 깊이 우선 탐색 
    visitedDfs[v] = 1
    print(v, end=" ")

    # 간선이 있고, 방문하지 않았으면 dfs 호출 
    for i in range(1, n+1):
        if (matrix[v][i] and (not visitedDfs[i])):
            dfs(i)
    
def bfs(v):   # 너비 우선 탐색 
    dq = deque([v])
    visitedBfs[v] = 1

    while(dq):
        v = dq.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if (matrix[v][i] and (not visitedBfs[i])):
                dq.append(i)
                visitedBfs[i] = 1

dfs(v)
print()
bfs(v)