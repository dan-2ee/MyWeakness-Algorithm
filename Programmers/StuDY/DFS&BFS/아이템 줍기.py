from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    matrix = [[-1]*102 for _ in range(102)]
    visited = [[1]*102 for _ in range(102)]
    # 사각형 내부는 0, 외부는 -1, 테두리는 1
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if (x1 < i < x2 and y1 < j < y2): # 내부인 경우 0으로 채움
                    matrix[i][j] = 0
                elif (matrix[i][j] != 0):  # 테두리는 1로 채움 
                    matrix[i][j] = 1
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    dq = deque()
    answer = 0
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    dq.append((cx, cy))
    
    while (dq):
        x, y = dq.popleft()
        if (x == ix and y == iy):
            # 경로에 2배 했으니 2로 나눠줌 
            answer = visited[x][y] // 2
            break
        for i in range(4):
            dx, dy = x+directions[i][0], y+directions[i][1]
            if (matrix[dx][dy] == 1 and visited[dx][dy] == 1):
                visited[dx][dy] = visited[x][y]+1
                dq.append((dx, dy))
    return answer