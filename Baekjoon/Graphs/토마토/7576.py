import sys
from collections import deque

# using BFS
def countDay():
    # 상하좌우 방향 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(ripeTomatos):
        x, y = ripeTomatos.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and matrix[nx][ny]==0):
                ripeTomatos.append((nx, ny))
                matrix[nx][ny] = matrix[x][y]+1
    
    # 토마토가 모두 익을 수는 없는 경우 (아직 익지 않은 토마토가 남아있는 경우)
    for i in range(n):
        if (0 in matrix[i]):
            return -1
    
    maxValue = max(map(max, matrix))
    # maxValue = 1 : 저장될때부터 모든 토마토가 익어있는 경우
    # maxValue = other : 모든 토마토가 익은 경우
    return (0 if maxValue == 1 else maxValue-1)
    
m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    # 토마토의 상태 저장 
ripeTomatos = deque([(i, j) for i in range(n) for j in range(m) if (matrix[i][j]==1)])  # 익은 토마토의 위치 저장

print(countDay())
