import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))
distance = [h-y, y, x, w-x]
print(min(distance))
