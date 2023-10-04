import sys
import heapq

input = sys.stdin.readline
T = int(input()) 

for _ in range(T):
    N = int(input())
    minHeap, maxHeap = [], []  # maxHeap 은 부호 반대로 저장 
    isExist = [False] * N
    for id in range(N):
        command, num = input().split() 
        num = int(num)
        if command == "I":
            heapq.heappush(minHeap, (num, id))
            heapq.heappush(maxHeap, (-num, id))
            isExist[id] = True
        elif num == 1:
            while maxHeap and not isExist[maxHeap[0][1]]:
                heapq.heappop(maxHeap)
            if maxHeap:
                isExist[maxHeap[0][1]] = False
                heapq.heappop(maxHeap)
        else:
            while minHeap and not isExist[minHeap[0][1]]:
                heapq.heappop(minHeap)
            if minHeap:
                isExist[minHeap[0][1]] = False
                heapq.heappop(minHeap)

    while minHeap and not isExist[minHeap[0][1]]:
        heapq.heappop(minHeap) 

    while maxHeap and not isExist[maxHeap[0][1]]:
        heapq.heappop(maxHeap) 

    print(-maxHeap[0][0], minHeap[0][0]) if maxHeap and minHeap else print("EMPTY")