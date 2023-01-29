import sys

n = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in info:
    k = 0
    for j in info:
        # 키, 몸무게 모두 커야함 (같으면 비교 붏가)
        if (i[0] < j[0] and i[1] < j[1]):
            k+=1
    print(k+1, end=" ")