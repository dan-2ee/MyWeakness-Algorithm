import sys
from collections import deque

def bfs(r, c):
    dq = deque([(r,c)])
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    cnt = 1
    map[r][c] = 2 # 시작 노드 방문 처리
    while dq:
        x,y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (0<=nx<N and 0<=ny<N and map[nx][ny]==1):
                cnt+=1
                map[nx][ny] = 2 # 방문처리
                dq.append((nx,ny))
    return cnt

input = sys.stdin.readline
N = int(input())
map = []
for _ in range(N):
    map.append([int(s) for s in input().rstrip()])
answer = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
for a in sorted(answer):
    print(a)