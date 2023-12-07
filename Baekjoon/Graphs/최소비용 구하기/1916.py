import sys
import heapq

def dijkstra(start):
    distance[start] = 0
    # heapq 사용
    # [비용, 노드] 로 넣음 - 비용이 작은 순으로 정렬
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        cost, node = heapq.heappop(queue)
        if cost > distance[node]:
            continue

        for next_node, next_cost in matrix[node]:
            if (distance[next_node] > cost + next_cost):
                distance[next_node] = cost + next_cost
                heapq.heappush(queue, [distance[next_node], next_node])

input = sys.stdin.readline
N = int(input())
M = int(input())
matrix = [[] for _ in range(N+1)]
INF = sys.maxsize
distance = [INF] * (N+1)

for _ in range(M):
    start, end, dist = map(int, input().split())
    matrix[start].append([end, dist])

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])