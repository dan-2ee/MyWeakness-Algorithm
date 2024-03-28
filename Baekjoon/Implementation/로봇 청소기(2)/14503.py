import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 좌표, 방향 
d = (4-d) if d else 0  # 북, 서, 남, 동 순서로 맞춤
map = [list(map(int, input().split())) for _ in range(N)]
front = [(-1,0), (0,-1), (1,0), (0,1)]  # 전진 
back = [(1,0), (0,1), (-1,0), (0,-1)]  # 후진
direction = [(1,0), (-1,0), (0,1), (0,-1)]  # 주변 네칸 
cnt = 0

def isDirty(r, c):
    for x, y in direction:
        if map[r+x][c+y] == 0:  # 주변에 청소안된 곳이 있는 경우 
            return 1
    return 0

while (True):
    if map[r][c] == 0:
        map[r][c] = 2  # 청소하면 2로 표시 
        cnt += 1  
    if (isDirty(r,c)):  # 청소되지 않은 빈칸이 있는 경우 
        d = (d+1)%4  # 반시계 방향 90도 회전 
        x, y = front[d]
        if (map[r+x][c+y] == 0):  # 바라보는 방향의 앞이 빈칸일 경우 
            r,c = r+x, c+y   # 한 칸 전진 
    else:  # 청소되지 않은 빈칸이 없는 경우 
        x, y = back[d]
        if map[r+x][c+y] != 1:  # 후진할 수 있으면 후진 
            r, c = r+x, c+y
        else:
            break

print(cnt)