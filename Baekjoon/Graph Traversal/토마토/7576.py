import sys
from collections import deque

def bfs():
    while tomato:
        x,y = tomato.popleft()  # 현재 익은 토마토의 위치 
        for dx, dy in directions:
            nx, ny = x+dx, y+dy   # 검사할 위치 
            if (0<=nx<N and 0<=ny<M and box[nx][ny]==0):
                tomato.append((nx,ny))
                box[nx][ny] = box[x][y]+1  # 하루 지남 
    
    for i in range(N):
        if 0 in box[i]: return -1  # 모든 토마토가 익지 못하는 경우 

    return max(max(box[i]) for i in range(N))-1  # 처음 토마토가 1일로 기록되어있으므로 -1 

input = sys.stdin.readline
M, N = map(int, input().split()) # 가로, 세로
box = [list(map(int, input().split())) for _ in range(N)]
tomato = deque([(i,j) for i in range(N) for j in range(M) if box[i][j] == 1])  # 초기에 익어있는 토마토의 위치
directions = [(1,0), (-1,0), (0,1), (0,-1)]
print(bfs())