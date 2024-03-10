import sys

def dfs(node, visited):
    global matrix
    visited[node] = 1
    count = 1
    for idx in range(1, len(matrix)):
        if (not visited[idx] and matrix[node][idx]):
            count += dfs(idx, visited)
    return count

def solution(n, wires):
    global matrix
    matrix = [[0]*(n+1) for _ in range(n+1)]
    
    for wire in wires:
        matrix[wire[0]][wire[1]], matrix[wire[1]][wire[0]] = 1, 1
    
    answer = sys.maxsize
    for wire in wires:
        visited = [0]*(n+1)
        matrix[wire[0]][wire[1]], matrix[wire[1]][wire[0]] = 0, 0
        cnt = dfs(1, visited)
        # cnt: 전력망1이 가지고 있는 송전탑 개수
        # n-cnt: 전력망2가 가지고 있는 송전탑 개수
        answer = min(answer, abs(cnt- (n-cnt)))
        # 원상복귀
        matrix[wire[0]][wire[1]], matrix[wire[1]][wire[0]] = 1, 1
        
    return answer