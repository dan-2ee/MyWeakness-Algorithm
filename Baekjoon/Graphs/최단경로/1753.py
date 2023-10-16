import sys

INF = sys.maxsize
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
matrix = [[]*(V+1) for _ in range(V+1)]
visited = [0]*(V+1)
distance = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    matrix[u].append((v, w))

def SmallestNode():
    idx = 0
    minValue = INF
    for i in range(1, V+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            idx = i
    return idx

def Dijkstra(start):
    visited[start] = 1
    for node in matrix[start]:
        distance[node[0]] = node[1]
    
    for _ in range(V-1):
        next = SmallestNode()
        visited[next] = 1
        for node in matrix[next]:
            if distance[node[0]] > distance[next] + node[1]:
                distance[node[0]] = distance[next] + node[1]
    distance[start] = 0  # 시작 노드의 가중치는 0 


Dijkstra(start)
for i in distance[1:]:
    print(i) if i != INF else print("INF")
