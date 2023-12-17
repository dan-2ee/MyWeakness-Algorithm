import sys

def bfs():
    global cnt
    queue = set([(0, 0, lst[0][0])])

    while queue:
        x, y, route = queue.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < R and 0 <= ny < C):
                if (lst[nx][ny] not in route):
                    queue.add((nx, ny, lst[nx][ny] + route))
        cnt = max(cnt, len(route))

input = sys.stdin.readline
R, C = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]
cnt = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs()
print(cnt)