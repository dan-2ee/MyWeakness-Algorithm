import sys, copy
from itertools import combinations
from collections import deque

def bfs():
    copyMap = copy.deepcopy(map)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우
    queue = deque(virus[:])

    while (queue):
        x, y = queue.popleft()
        for dir in directions:
            dx, dy = x+dir[0], y+dir[1]
            if (0<=dx<N and 0<=dy<M and copyMap[dx][dy] == 0):
                copyMap[dx][dy] = 2
                queue.append((dx, dy))
    
    return sum(copyMap[i].count(0) for i in range(N))

input = sys.stdin.readline
N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
empty = []   # 벽을 세울 수 있는 위치 
virus = []   # 바이러스의 위치

for i in range(N):
    for j in range(M):
        if (map[i][j] == 2): virus.append((i,j))
        elif (map[i][j] == 0): empty.append((i,j))

answer = 0
for comb in combinations(empty, 3):
    # 벽을 세움 
    for x, y in comb:
        map[x][y] = 1
    answer = max(answer, bfs())
    # 벽 없앰
    for x, y in comb:
        map[x][y] = 0

print(answer)