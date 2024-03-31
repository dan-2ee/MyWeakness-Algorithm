import sys
from collections import deque

def bfs():
    dq = deque([(0,0)])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while dq:
        r, c = dq.popleft()
        if (r==N-1 and c==M-1):
            break
        for x, y in directions:
            dx, dy = r+x, c+y
            if (0<=dx<N and 0<=dy<M):
                if (map[dx][dy]==1 or map[dx][dy] > map[r][c]+1):
                    dq.append((dx,dy))
                    map[dx][dy] = map[r][c]+1
    return map[N-1][M-1]

input = sys.stdin.readline
N, M = map(int, input().split())
map = []
for _ in range(N):
    map.append([int(s) for s in input().strip()])

print(bfs())