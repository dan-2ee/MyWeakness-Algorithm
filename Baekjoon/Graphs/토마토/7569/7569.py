import sys
from collections import deque

def bfs():
    while(ripeTomato):
        h, y, x = ripeTomato.popleft()
        # 한칸 위, 한칸 아래, 상, 하, 좌, 우
        directions = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
        for direct in directions:
            dh, dy, dx = h+direct[0], y+direct[1], x+direct[2]
            if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
                if tomato[dh][dy][dx] == 0:
                    tomato[dh][dy][dx] = tomato[h][y][x] + 1
                    ripeTomato.append([dh, dy, dx])
    
input = sys.stdin.readline
M, N, H = list(map(int, input().split()))
tomato = []
ripeTomato = deque([])  # 익은 토마토의 위치 저장 

for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    tomato.append(tmp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                ripeTomato.append([i,j,k])

bfs()
days = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                sys.exit()
            days = max(days, tomato[i][j][k])
print(days-1)