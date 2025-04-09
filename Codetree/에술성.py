from collections import deque 

N = int(input()) # 무조건 홀수 
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
count_number = [0] * (N*N+1) # 그룹별 숫자의 개수 
numbering_board = [[0]* N for _ in range(N)]  # 숫자로 바꾼 보드
group_number = 0 # 그룹의 개수 
final_score = 0  # 최종 예술 점수 

dx = [-1,1,0,0] # 상하좌우 방향
dy = [0,0,-1,1]

def rotate_square(x,y,stdr,rotated_board):
    for i in range(x,x+stdr):
        for j in range(y,y+stdr):
            ox, oy = i-x, j-y  # 원점 맞추기 
            nx, ny = oy, stdr-ox-1
            rotated_board[nx+x][ny+y] = board[i][j]

def rotate_board():   # 보드 회전 
    global board
    rotated_board = [[0]*N for _ in range(N)] # 회전된 보드
    stdr = N//2  # 중심
    for i in range(N):   # 십자 모양 회전 
        rotated_board[stdr][i] = board[i][stdr]  # 십자 모양 세로 
        rotated_board[N-i-1][stdr] = board[stdr][i]  # 십자 모양 가로
    
    # 정사각형 네개 회전 
    rotate_square(0,0,stdr,rotated_board)
    rotate_square(0,0+stdr,stdr,rotated_board)
    rotate_square(0+stdr,0,stdr,rotated_board)
    rotate_square(0+stdr,0+stdr,stdr,rotated_board)
    # 회전된 보드로 갱신
    board = rotated_board

def isSafe(x,y):
    return 0<=x<N and 0<=y<N

def bfs(x,y):
    global visited, count_number, numbering_board
    dq = deque([(x,y)])
    while dq:
        x,y = dq.popleft()
        visited[x][y] = 1
        for i in range(4):  # 상하좌우 탐색 
            nx,ny = x+dx[i], y+dy[i]
            if isSafe(nx,ny) and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                dq.append((nx,ny))
                visited[nx][ny] = 1
                count_number[group_number] += 1
                numbering_board[nx][ny] = group_number
    
def make_board():
    global visited, group_number, count_number, numbering_board
    # 변수 초기화
    visited = [[0]* N for _ in range(N)]
    group_number = 0
    #count_number = [0] * (N*N+1)
    numbering_board = [[0]* N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                group_number += 1 # 그룹 개수 추가 
                count_number[group_number] = 1
                numbering_board[i][j] = group_number
                bfs(i,j)

def get_score():   # 예술 점수 계산 
    make_board() 
    score = 0
    for x in range(N):
        for y in range(N):
            for n in range(4):
                nx,ny = x+dx[n], y+dy[n]
                # (x,y) (nx,ny)가 다른 그룹일 경우 
                if isSafe(nx,ny) and board[x][y] != board[nx][ny]:
                    a, b = numbering_board[x][y], numbering_board[nx][ny]
                    score += (count_number[a]+count_number[b])*board[x][y]*board[nx][ny]
    # 조합 하나당 두번 계산 되었으므로 2로 나눔 
    return score//2 

for n in range(4):
    tmp = get_score()
    final_score += tmp
    if n != 3:  # 3회전하지 않은 경우 
        rotate_board()  # 보드 회전 
    print(n)
    print(board)
    

print(final_score)