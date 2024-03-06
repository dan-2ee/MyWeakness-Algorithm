from collections import deque

def BFS(maps):
    n, m = len(maps), len(maps[0]) # n: 세로. m: 가로
    dq = deque([(0,0)])  # 방문할 노드들 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    
    while(dq):
        x, y = dq.popleft()
        if (x == n-1 and y == m-1):   # 진영 도착
            return maps[x][y]
        for item in directions:
            dx, dy = x+item[0], y+item[1]
            if (0 <= dx < n and 0 <= dy < m):
                # 길이 있으면(maps[dx][dy]=1: 방문하지 않은 경우 체크) queue 에 추가
                if (maps[dx][dy] == 1):
                    dq.append((dx,dy))
                    maps[dx][dy] = maps[x][y]+1
    # 상대팀 진영에 도착할 수 없는 경우 -1 리턴
    return -1
def solution(maps):
    return BFS(maps)