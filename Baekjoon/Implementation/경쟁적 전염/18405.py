import sys
from collections import deque 

def multiplyVirus():
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  
    while (virusDq):
        virus, t, x, y = virusDq.popleft()
        if (t == S):
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0):
                graph[nx][ny] = virus
                virusDq.append([virus, t+1, nx, ny])


input = sys.stdin.readline           
N, K = map(int, input().split())
graph = []
virusLst = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if (graph[i][j]):
            # 바이러스, 시간, x, y
            virusLst.append([graph[i][j], 0, i, j])

virusLst.sort()
virusDq = deque(virusLst)
S, X, Y = map(int, input().split())

multiplyVirus()
print(graph[X-1][Y-1])