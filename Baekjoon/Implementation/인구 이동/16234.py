import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(r, c):
    visited[r][c] = 1
    dq = deque([(r, c)])
    loc = [(r,c)]  # 국경선이 열린 곳의 위치
    global ismove
    while (dq):
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (0<=nx<N and 0<=ny<N and not visited[nx][ny]):
                if (L <= abs(map[x][y] - map[nx][ny]) <= R):
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                    loc.append((nx, ny))
    if len(loc) > 1: ismove = 1  # 인구 이동이 발생한 경우 

    # 국경선 모두 열었으면 인구 이동 시킴 
    people = sum(map[x][y] for x, y in loc) // len(loc) # 각 칸의 인구수 
    for nx, ny in loc:
        map[nx][ny] = people
    
    
day = 0
while (1):
    visited = [[0]*N for _ in range(N)]
    global ismove  # 이동이 일어났는지 체크
    ismove = 0
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == 0):
                bfs(i, j)
    if not ismove:  # 이동이 없으면 끝남 
        break
    day += 1

print(day)