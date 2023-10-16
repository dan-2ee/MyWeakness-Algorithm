import sys

INF = sys.maxsize
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
matrix = [[INF]*(V+1) for _ in range(V+1)]
visited = [0]*(V+1)
distance = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    matrix[u][v] = w

def SmallestNode():
    idx = 0
    minValue = INF
    for i, value in enumerate(distance):
        if value < minValue and not visited[i]:
            minValue = value
            idx = i
    return idx

def Dijkstra(start):
    visited[start] = 1
    for i, v in enumerate(matrix[start]):
        distance[i] = v
    
    for _ in range(V-1):
        next = SmallestNode()
        visited[next] = 1
        for idx, value in enumerate(matrix[next]):
            if distance[idx] > distance[next] + value:
                distance[idx] = distance[next] + value
    distance[start] = 0  # 시작 노드의 가중치는 0 
    
    for i in distance[1:]:
        print(i) if i != INF else print("INF")

Dijkstra(start)
