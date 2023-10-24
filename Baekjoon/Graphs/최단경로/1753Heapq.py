# 다익스트라 heapq 사용 구현
import sys
import heapq 

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

def Dijkstra(start):
    visited[start] = 1
    q = []
    # (비용, 노드 번호) 로 저장
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        for next in matrix[node]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


Dijkstra(start)

for i in distance[1:]:
    print(i) if i != INF else print("INF")
