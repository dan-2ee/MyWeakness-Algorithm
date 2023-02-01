import sys
from collections import deque

def countComputer():
    dq = deque([1])   # 1번 컴퓨터부터 시작 
    visited[1] = 1
    cnt = -1        # 1번 컴퓨터는 세지 않음 
    while(dq):
        computer = dq.popleft()
        cnt += 1
        for i in range(1, v+1):
            if (not visited[i] and matrix[computer][i]):
                dq.append(i)
                visited[i] = 1

    return cnt

v = int(sys.stdin.readline())
n = int(sys.stdin.readline())
matrix = [[0]*(v+1) for _ in range(v+1)]  # 인덱스 1은 사용하지 않음 
visited = [0] * (v+1)

for _ in range(n):
    v1, v2 = map(int, sys.stdin.readline().split())
    matrix[v1][v2] = matrix[v2][v1] = 1

print(countComputer())

