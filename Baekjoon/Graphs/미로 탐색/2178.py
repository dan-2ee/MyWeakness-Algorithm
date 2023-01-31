import sys
from collections import deque

def dfs(row, col):  
    dq = deque([(row, col)])

    # 상하좌우 순서
    dx = [-1, 1, 0, 0]  # x direction
    dy = [0, 0, -1, 1]  # y direction

    while (dq):
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1):
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append((nx, ny))
    return matrix[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

print(dfs(0, 0))  # (0, 0)부터 시작 