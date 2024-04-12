import copy 

dx = [-1,0,1,0]  # 상우하좌 순서 
dy = [0,1,0,-1]

# 이미 다른 기사의 영역인지 체크 
def is_knight_area(copy_knights_area,knight_number,x,y):
    # 빈공간이 아니면서, 자신의 영역도 아니면 이미 다른 기사가 있으므로 True
    if copy_knights_area[x][y]==0:
        return 0
    elif copy_knights_area[x][y]==knight_number:
        return 0
    else:
        return copy_knights_area[x][y]

def whos_area(copy_knights_area,knight_number,x,y,h,w):
    masters = []
    for i in range(x,x+h):
        for j in range(y,y+w):
            k = is_knight_area(copy_knights_area,knight_number,i,j)
            if k and k not in masters:  # 이미 다른 기사의 영역인 경우, 기사 번호 리턴 
                masters.append(k)
    return masters if masters!=[] else []

def color_knight_area(copy_knights_area,kn,tx,ty,th,tw): # knight_area 이동구역으로 칠함  
    for i in range(tx, tx+th):
        for j in range(ty, ty+tw):
            copy_knights_area[i][j] = kn  

def remove_knight_area(x,y,h,w):  # 목숨이 끝난 기사의 영역을 지움 
    global knight_area
    for i in range(x,x+h):
        for j in range(y,y+w):
            knight_area[i][j] = 0

def remove_copy_knight_area(copy_knights_area,kn,x,y,h,w): # 이전 영역을 지움 
    for i in range(x,x+h):
        for j in range(y,y+w):
            if copy_knights_area[i][j] == kn: # 내 구역일때만 지움 
                copy_knights_area[i][j] = 0

def is_safe_range(x,y):
    return 1<=x<=L and 1<=y<=L

def is_safe_area(x,y,h,w):
    # 해당 구역이 안전한 구역인지 체크 
    for i in range(x,x+h):
        for j in range(y,y+w):
            # 체스판 밖도 벽으로 간주
            if (not is_safe_range(i,j)) or (board[i-1][j-1]==2):  # 범위를 벗어났거나 벽이 있는 경우 false, board 체크는 인덱스 다름 
                return False
    return True 

def check_damage(knight_number, k):
    global damage, knights
    # k 기사를 함정만큼 라이프 줄임 
    # 라이프 -1이면 죽은 기사 
    if knight_number == k:  # knight_number: 명령을 받은 기사, 데미지 입지 않음 
        return 
    tmp_life = 0   # 함정의 개수 
    x,y,h,w,life = knights[k]
    for r in range(x,x+h):
        for c in range(y,y+w):
            if board[r-1][c-1] == 1:  # board 인덱스가 하나 작음 
                tmp_life+=1
    if life - tmp_life <=0:
        remove_knight_area(x,y,h,w)
        knights[k][4] = -1  # 목숨보다 많은 데미지 입으면 생명 -1처리
    else:
        damage[k] += tmp_life
        knights[k][4] -= tmp_life
    

def move_knight(knight_number, d):
    global knights, knight_area
    x,y,h,w,life = knights[knight_number]
    nx, ny = x+dx[d],y+dy[d] # 한칸 밀려서 바뀔 시작 위치 
    if not is_safe_area(nx,ny,h,w):  # 밀린 위치에서 구역을 만들지 못하는 경우 
        return 
    else:  # 영역을 만들 수 있는 경우 
        copy_knights = copy.deepcopy(knights) # 벽을 만날 경우 되돌려야하기 때문에 복사해서 사용 
        copy_knights_area = copy.deepcopy(knight_area)
        kn, tx, ty, th, tw, tl = knight_number,nx,ny,h,w,life # 이동할 나이트 정보 
        is_safe = 1
        stack = [kn]  # 현재 이동할 나이트
        move_knight_lst = set([kn])
        processed_knight = []  # 이미 이동한 나이트
        while stack:
            kn = stack.pop(0) # 현재 움직이는 기사 
            if kn in processed_knight:
                continue
            processed_knight.append(kn)
            tx, ty, th, tw, tl = copy_knights[kn][0]+dx[d], copy_knights[kn][1]+dy[d], copy_knights[kn][2], copy_knights[kn][3], copy_knights[kn][4]
            if not is_safe_area(tx,ty,th,tw):  # 이동할 영역이 체스판 밖인지 체크
                is_safe = 0
                break
            master = whos_area(copy_knights_area, kn,tx,ty,th,tw)  # 이동할 영역의 주인 
            stack.extend(master)  # 이동할 기사 추가 
            move_knight_lst.update(master)

            # 이전 구역 지우고 # 복사된 구역에 이동범위로 다시 칠함 
            remove_copy_knight_area(copy_knights_area,kn,copy_knights[kn][0],copy_knights[kn][1],copy_knights[kn][2],copy_knights[kn][3])
            color_knight_area(copy_knights_area,kn,tx,ty,th,tw) 
            copy_knights[kn] = [tx, ty, th, tw, tl] # 좌표 이동
            
        if is_safe:  # 이동이 안전하게 끝난 경우
            knights = copy.deepcopy(copy_knights)  # 기사 정보 바꿔줌 
            knight_area = copy.deepcopy(copy_knights_area)  # 구역 정보 바꿔줌
            for k in move_knight_lst:
                check_damage(knight_number, k) # 함정이랑 비교해서 데미지 체크
        else: # 이동이 안전하게 끝나지 못한 경우, 이동 무효
            return 


L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)] # 체스판
global knights, knight_area

knights = [[0,0,0,0,0]] # 기사들의 정보 (x,y,h,w,목숨)
damage = [0]*(N+1)

for _ in range(N):
    knights.append(list(map(int, input().split())))
knight_area = [[0]*(L+1) for _ in range(L+1)] # 기사들의 영역 
for i in range(1,N+1):
    x,y,h,w,_ = knights[i]
    for x1 in range(x,x+h):
        for y1 in range(y,y+w):
            knight_area[x1][y1] = i # 기사 번호로 영역 표시 


# Q 개의 명령 실행 
for _ in range(Q):
    knight_number, d = map(int, input().split()) # 이동할 기사 번호, 방향 
    # 체스판에서 사라진 기사가 아닐 경우에만 이동할 수 있음
    if knights[knight_number][4] != -1:  # 체스판에서 사라졌는지 체크
        move_knight(knight_number, d)
answer = 0
for i in range(1,N+1):
    if knights[i][4] != -1:
        answer += damage[i]

print(answer)