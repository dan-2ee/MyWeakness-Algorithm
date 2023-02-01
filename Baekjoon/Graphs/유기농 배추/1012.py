import sys
from collections import deque

def countWorm(startX, startY):
    dq = deque([(startX, startY)])
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while(dq):
        x, y = dq.popleft()
        # 방문한 배추의 위치 삭제 
        if ((x,y) in cabbages):
            cabbages.remove((x, y))
        #상하좌우로 갈 수 있는 길 탐색 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 ):
                dq.append((nx, ny))
                matrix[nx][ny] = matrix[x][y]+1

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0]*(m) for _ in range(n)]    # 배추의 위치 matrix 위에 표시 
    cabbages = deque()     # 배추의 위치 (x, y) 형태로 저장 
    cntWorm = 0
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        cabbages.append((x, y))

    while(cabbages):
        x, y = cabbages.popleft()
        countWorm(x, y)    # 인접한 위치의 배추 모두 탐색 
        cntWorm += 1
    
    print(cntWorm)