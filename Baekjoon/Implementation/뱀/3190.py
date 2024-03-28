import sys
import heapq 
from collections import deque

input = sys.stdin.readline
N = int(input()) # 보드의 크기 
K = int(input()) # 사과 개수 
apples = [list(map(int, input().split())) for _ in range(K)] # 사과 위치 
L = int(input()) # 방향 변환 횟수
command = []
for _ in range(L):
    n, s = input().split()
    heapq.heappush(command, (int(n), s))
r, c = 1, 1  # 머리의 위치 
time, d = 0, 1 # 동쪽 방향으로 시작 
directions = [(-1,0), (0,1), (1,0), (0,-1)]   # 북 동 남 서 
visited = deque([(r,c)])  # 뱀 위치

while (True):
    time += 1
    nr, nc = r+directions[d][0], c+directions[d][1]  # 이동할 위치 
    
    if (0 >= nr or nr > N or 0 >= nc or nc > N): break # 벽인 경우 
    if ((nr, nc) in visited): break # 몸인 경우
    elif ([nr, nc] in apples): apples.remove([nr,nc]) # 사과가 있을 경우 
    else: visited.popleft() # 사과가 없는 경우 꼬리 이동 

    visited.append((nr, nc))
    r, c = nr, nc  # 머리 이동 
    # 방향 전환 
    if (command and command[0][0] == time):
        _, dir = heapq.heappop(command)
        if (dir == "D"): d = (d+1)%4
        else: d = (d-1)%4
print(time)