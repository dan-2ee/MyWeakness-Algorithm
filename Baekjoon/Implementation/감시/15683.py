import sys
import copy

def mask(map, dir, x, y):
    # dir = cctv 방향 , x,y: cctv 위치
    for d in dir:
        dx, dy = x, y
        while True:
            # 방향에 있는 모든 0칸 -1로 바꿈 
            dx, dy = dx+directions[d][0], dy+directions[d][1]
            if (dx<0 or dy<0 or dx>=N or dy>=M):
                break
            if (map[dx][dy]==6):  # 벽인 경우
                break
            elif (map[dx][dy]==0):  # 빈공간인 경우 
                map[dx][dy] = -1 # 마스킹 
        
def dfs(depth, map):
    global answer
    if depth == len(cctv):
        # 모든 cctv를 한번씩 검사한 경우 
        cnt = 0
        for i in range(N):
            cnt += map[i].count(0)
        answer = min(answer, cnt)  # 사각지대 최솟값으로 갱신 
    else:
        copy_map = copy.deepcopy(map)
        num, x, y = cctv[depth] # 검사할 cctv 번호, 위치
        for dir in rotate[num]:
            mask(copy_map, dir, x, y)
            dfs(depth+1, copy_map)
            # len(cctv)-1 개 만큼 점검한 상태
            copy_map = copy.deepcopy(map)

input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cctv = [(map[i][j], i, j) for i in range(N) for j in range(M) if map[i][j]!=0 and map[i][j]!=6] # cctv 번호, x, y 

directions = [(-1,0), (0,1), (1,0), (0,-1)] # 북동남서
rotate = [
    [0],
    [[0], [1], [2], [3]],  # 1번 cctv 가능한 방향 
    [[0,2], [1,3]],  # [0,2] => 2번 cctv 방향: 북남
    [[0,1], [1,2], [2,3], [3,0]],
    [[1,2,3], [0,2,3], [0,1,3], [0,1,2]],
    [[0,1,2,3]]
]
global answer
answer = sys.maxsize
dfs(0, map)
print(answer)