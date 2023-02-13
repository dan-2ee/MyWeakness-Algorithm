import sys
from heapq import heappush, heappop

t = int(sys.stdin.readline())
hq = []

for _ in range(t):
    n = int(sys.stdin.readline())
    if (n):
        heappush(hq, (abs(n), n))   # 절댓값으로 정렬 
    else:          
        print(heappop(hq)[1]) if (hq) else print(0)