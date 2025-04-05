import copy 
from collections import deque

rotatable = [[1,1],[2,1],[3,1], [1,2],[2,2],[3,2], [1,3],[2,3],[3,3]]   # 회전 가능한 중심 좌표 
angle = [90,180,270] # 회전 가능한 각도 
dx = [-1,1,0,0]  # 상하좌우
dy = [0,0,-1,1]  

def fill_wall(wall):  # 비워진 유물 채우기 (0으로 비움)
    # x값이 크고 y값이 작은 순서
    global relic_piece
    for i in range(5):
        for j in range(4,-1,-1):
            if wall[j][i] == 0:
                wall[j][i] = relic_piece.popleft()
    return wall

def count_score(wall):  # 유물 조각 개수 확인 
    visited = [[0]*5 for _ in range(5)]
    score = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                dq, trace = deque([(i,j)]), deque([(i,j)])  # trace: 이동 경로(좌표)
                while dq:
                    x,y = dq.popleft()
                    visited[x][y] = 1
                    for n in range(4):
                        nx, ny = x+dx[n], y+dy[n]  # 이동할 좌표 
                        # 기준좌표와 같은 값이고 방문하지 않았을 경우
                        if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and (wall[x][y]==wall[nx][ny]): 
                            dq.append((nx,ny))  
                            trace.append((nx,ny))  # 경로 추가 
                            visited[nx][ny] = 1
                if len(trace)>=3:   # 3개 이상 연결된 경우 
                    score+=len(trace)  # 점수 더함 
                    while trace:
                        x,y = trace.popleft()
                        wall[x][y] = 0   # 획득한 유물 지워줌 
    return score
            
def rotation_wall(x,y,angle):  # 3x3 회전
    global wall
    copy_wall = copy.deepcopy(wall)  # 회전된 배열 
    rotated_wall = [copy_wall[i][y-1:y+2] for i in range(x-1, x+2)]  # x,y 기준 3x3 배열
    
    if angle == 90: # 시계 방향 90도 회전 
        rotated_wall = list(map(list, zip(*rotated_wall[::-1])))  # 시계 방향 90도 회전 
    elif angle == 180: # 시계 방향 180도 회전 
        for _ in range(2):
            rotated_wall = list(map(list, zip(*rotated_wall[::-1])))
    else:  # 시계 방향 270도 회전 
        for _ in range(3):
            rotated_wall = list(map(list, zip(*rotated_wall[::-1])))
    cnt = 0
    # 회전한 배열로 바꿈 
    for i in range(x-1, x+2):
        copy_wall[i][y-1:y+2] = rotated_wall[cnt]
        cnt+=1
    return copy_wall  # 회전된 배열 리턴 5x5    
 
global wall, max_relic  # 벽, 유물 최대 개수 
K, M = map(int, input().split())  # 탐사 횟수, 새로 생길 유물 개수
wall = [list(map(int, input().split())) for _ in range(5)] 
relic_piece = deque(map(int, input().split())) # 새로 생길 유물 번호 리스트, 생기면 사라짐 

for _ in range(K):  
    max_score, tmp_angle, tmp_wall = 0,360,[]   # 최대로 얻을 수 있는 점수, 현재 각도, 벽
    for i in range(9): 
        x,y = rotatable[i]   # 중심 좌표
        for a in angle:
            rotated_wall = rotation_wall(x,y,a) # 회전된 배열
            score = count_score(rotated_wall)  # 조각 개수 확인 
            # 우선순위: 최대 점수, 각도, 좌표 
            if score > max_score:  
                max_score, tmp_angle, tmp_wall = score, a, rotated_wall  
            elif score != 0 and score == max_score and tmp_angle > a:  # 점수는 같지만 각도가 더 작은 경우 갱신
                max_score, tmp_angle, tmp_wall = score, a, rotated_wall  
                 
    if tmp_wall == []:  # 탐사에서 유물을 얻지 못한 경우
        break   # 종료
    wall = tmp_wall
    # 유물 연쇄 획득
    while True:
        wall = fill_wall(wall)   # 0으로 지워진 유물 채워줌  
        score = count_score(wall)
        if score == 0:  # 더 이상 얻을 수 있는 점수가 없는 경우 
            break
        max_score += score
    print(max_score, end=" ")