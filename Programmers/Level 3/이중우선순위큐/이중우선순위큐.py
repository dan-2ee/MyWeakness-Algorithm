import heapq

def solution(operations):
    minHeap, maxHeap = [], []
    for operation in operations:
        command, num = operation.split()
        if command == "I":
            heapq.heappush(minHeap, int(num))
            heapq.heappush(maxHeap, -1*int(num))
        elif num == "1" and minHeap:
            maxnum = heapq.heappop(maxHeap)
            minHeap.remove(-1*maxnum)
        elif num == "-1" and minHeap:
            minnum = heapq.heappop(minHeap)
            maxHeap.remove(-1*minnum)
        else:
            pass
     
    return [0, 0] if not minHeap else [-maxHeap[0], minHeap[0]]