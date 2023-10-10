import sys

def dfs(start, depth):
    global result
    if depth == 4:
        result = True
        return
    visited[start] = True
    for idx in graphs[start]:
        if not visited[idx]:
            dfs(idx, depth+1)
            visited[idx] = False     
    
input = sys.stdin.readline
N, M = list(map(int, input().split()))   
graphs = [[] for _ in range(N)]
result = False

for _ in range(M):
    line = list(map(int, input().split()))
    graphs[line[0]].append(line[1])
    graphs[line[1]].append(line[0])

for i in range(N):
    visited = [False] * N
    dfs(i, 0)
    if result:
        print(1)
        sys.exit()
print(0)
