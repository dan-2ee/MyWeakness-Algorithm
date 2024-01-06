import sys
from collections import deque

def bfs():
    dq = deque([])
    dq.append((0,0,0))
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    while (dq):
        x, y, current = dq.popleft()
        if (x==N-1 and y==M-1):
            return visited[x][y][current]
        for dir in directions:
            nx, ny = x+dir[0], y+dir[1]
            if (0<=nx<N and 0<=ny<M):
                # 다음 칸이 벽이고, 현재 벽을 부시지 않았을 때 
                if (graph[nx][ny] == 1 and current == 0):
                    visited[nx][ny][1] = visited[x][y][current] + 1
                    dq.append((nx, ny, 1))
                # 다음 칸이 벽이 아니고, 방문하지 않았을 때 
                elif (graph[nx][ny] == 0 and visited[nx][ny][current] == 0):
                    visited[nx][ny][current] = visited[x][y][current] + 1
                    dq.append((nx, ny, current))
    return -1

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(bfs())