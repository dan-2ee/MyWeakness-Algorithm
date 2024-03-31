import sys

def dfs(node):
    visited[node] = 1
    global answer
    answer += 1
    for n in network[node][1:]:
        if not visited[n]:
            dfs(n)
        
input = sys.stdin.readline
N = int(input())  # 컴퓨터 수
T = int(input())  # 컴퓨터 쌍의 수 
network = [[0] for _ in range(N+1)]
visited = [0]*(N+1)

global answer
answer = 0
for _ in range(T):
    n, m = map(int, input().split())
    network[n].append(m)
    network[m].append(n)

dfs(1)
print(answer-1) # 시작노드까지 카운트되었으므로 -1