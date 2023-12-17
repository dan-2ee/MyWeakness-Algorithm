import sys
from itertools import combinations

def buildWall():
    global answer
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for coordinates in combinations(buildable, 3):
        copy_map = [i[:] for i in map]
        queue = [i[:] for i in infected]
        cnt = 0
        for x, y in coordinates:
            copy_map[x][y] = 1
        
        # bfs()
        while queue:
            x, y = queue.pop()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (0<=nx<N and 0<=ny<M and copy_map[nx][ny]==0):
                    copy_map[nx][ny] = 2
                    queue.append((nx, ny))
        for i in range(N):
            cnt += copy_map[i].count(0)
        
        answer = max(answer, cnt)

        
input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
buildable = []   # 벽을 세울 수 있는 구역
infected = []    # 바이러스가 있는 구역
for i in range(N):
    for j in range(M):
        if (map[i][j] == 2):
            infected.append((i, j)) 
        if (map[i][j] == 0):
            buildable.append((i, j))

answer = 0
buildWall()
print(answer)