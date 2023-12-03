import sys

input = sys.stdin.readline
N, M = map(int, input().split())
R, C, D = map(int, input().split())  
matrix = [list(map(int, input().split())) for _ in range(N)]
cleanCnt = 0

# 전진 
fx = [-1, 0, 1, 0]
fy = [0, 1, 0, -1]
# 후진 
bx = [1, 0, -1, 0]
by = [0, -1, 0, 1]

while True:
    # 현재 칸 확인 
    if (matrix[R][C] == 0):
        matrix[R][C] = 2
        cleanCnt += 1
    # 상하좌우 4칸 확인, 주변에 청소되지 않은 칸이 있는 경우 
    if (matrix[R+fx[0]][C+fy[0]]==0 or matrix[R+fx[1]][C+fy[1]]==0 or matrix[R+fx[2]][C+fy[2]]==0 or matrix[R+fx[3]][C+fy[3]]==0):
        # 90도 회전
        D = 3 if (D==0) else D - 1
        nr, nc = R+fx[D], C+fy[D]
        # 청소되지 않았으면 한칸 전진 
        if (matrix[nr][nc] == 0):
            R, C = nr, nc
    # 청소되지 않은 칸이 없는 경우 
    else:
        # 후진 할 수 있으면 한칸 후진
        nr, nc = R+bx[D], C+by[D] 
        if (matrix[nr][nc] != 1):
            R, C = nr, nc
        else:
            break
            
print(cleanCnt)