import sys
from collections import deque

def bfs(r, c):
    dq = deque([(r,c)])
    while dq:
        x,y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1:
                dq.append((nx, ny))
                field[nx][ny] = 2
    
input = sys.stdin.readline
T = int(input())
directions = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())  # 가로, 세로, 배추 개수
    field = [[0]*M for _ in range(N)]
    answer = 0  # 지렁이
    for _ in range(K):
        r, c = map(int, input().rstrip().split())
        field[c][r] = 1
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)
