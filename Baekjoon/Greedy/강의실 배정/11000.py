import sys
import heapq

n = int(sys.stdin.readline())
timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timeTable.sort()  # 시작순으로 정렬 

startTime = []
heapq.heappush(startTime, timeTable[0][1])

for time in timeTable[1:]:
    if (time[0] >= startTime[0]):
        heapq.heappop(startTime)
        heapq.heappush(startTime, time[1])
    else:
        heapq.heappush(startTime, time[1])
print(len(startTime))