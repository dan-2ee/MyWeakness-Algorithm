import sys

def dfs(r, c, cnt):
    global result
    result = max(cnt, result)
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if (0 <= x < R and 0 <= y < C ):
            if (lst[x][y] not in visited):
                visited.add(lst[x][y])
                dfs(x, y, cnt+1)
                visited.remove(lst[x][y])

input = sys.stdin.readline
R, C = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]
visited = set(lst[0][0])
result = 1
dfs(0, 0, 1)
print(result)

