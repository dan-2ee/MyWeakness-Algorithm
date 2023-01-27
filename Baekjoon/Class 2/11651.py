import sys

n = int(sys.stdin.readline())
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
coordinates.sort(key = lambda x: (x[1], x[0]))
for x, y in coordinates:
    print(x, y)