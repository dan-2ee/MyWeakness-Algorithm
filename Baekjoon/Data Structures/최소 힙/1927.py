import sys
from heapq import heappop, heappush

t = int(sys.stdin.readline())
heap = []

for _ in range(t):
    n = int(sys.stdin.readline())
    if (n):
        heappush(heap, n)
    else:
        print(heappop(heap)) if(heap) else print(0)

