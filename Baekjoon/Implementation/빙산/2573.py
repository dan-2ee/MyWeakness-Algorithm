import sys
from collections import deque

def bfs(r,c):
    visited[r][c] = 1
    dq = deque([(r,c)])
    melted_ice = []  # 높이가 줄어들 예정인 빙하 
    while dq:
        x,y = dq.popleft()
        blank = 0  # 인접한 빈칸의 개수
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if not matrix[nx][ny]:
                    blank += 1
                elif matrix[nx][ny] and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                
        if blank > 0: # 주변에 1개 이상의 빈칸이 있는 경우
            melted_ice.append((x, y, blank))    # 좌표, 줄어들 높이

    for x, y, change in melted_ice:
        matrix[x][y] = max(0, matrix[x][y] - change)
        if matrix[x][y] == 0:  # 제거해서 빈칸이 된 경우 
            deleted_ice.append((x,y))  # 삭제될 빙하에 추가

input = sys.stdin.readline
N, M = map(int, input().split())
directions = [(1,0), (-1,0), (0,1), (0,-1)]
matrix = [list(map(int, input().split())) for _ in range(N)]
ice = [(i,j) for i in range(N) for j in range(M) if matrix[i][j]]  # 빙하의 위치 
year = 0

while True:
    loc = 0  # 구역 개수 
    deleted_ice = []  # 삭제될 빙하 (=높이가 0으로 바뀐 빙하)
    visited = [[0]*M for _ in range(N)]
    for x, y in ice:
        if not visited[x][y]:
            bfs(x,y)
            loc+=1
    # 높이가 없어진 빙하 삭제 
    ice = list(set(ice) - set(deleted_ice))
    if loc >=2:
        print(year)
        break
    year+=1 
    if not ice:
        print(0)
        break
    