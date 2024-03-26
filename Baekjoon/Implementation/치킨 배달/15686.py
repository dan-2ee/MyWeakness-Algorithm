import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
homelst, chickenlst = [], []  # 집이 있는 위치, 치킨집이 있는 위치 
for i in range(N):
    for j in range(N):
        if (map[i][j] == 1): homelst.append((i,j))
        elif (map[i][j] == 2): chickenlst.append((i,j))

answer = sys.maxsize  # 치킨 거리의 최솟값
for item in combinations(chickenlst, M):
    # item: M개의 치킨집 위치
    distance = 0
    for homeX, homeY in homelst:
        distance += min(abs(homeX - chickenX)+abs(homeY - chickenY) for chickenX, chickenY in list(item))  # 집마다 치킨 거리 계산 
    answer = min(answer, distance)

print(answer)