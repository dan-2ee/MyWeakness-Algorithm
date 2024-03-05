def dfs(node, computers):
    global visited
    line = computers[node]
    # 방문 체크
    visited[node] = 1
    for idx, item in enumerate(line):
        # 노드를 방문하지 않았고, 연결되어있는 경우
        if (not visited[idx] and item == 1):
            dfs(idx, computers)
    
    
def solution(n, computers):
    global visited
    visited = [0] * n
    network = 0
    for node in range(n):
        if not visited[node]:
            dfs(node, computers)
            # 시작 노드에 연결 되어 있는 모든 노드 방문 체크
            # 네트워크 += 1
            network += 1
    
    return network