import heapq

def solution(operations):
    maxhq, minhq = [], []
    for operation in operations:
        oper, num = operation.split()
        if (oper == "I"):
            heapq.heappush(maxhq, -int(num))
            heapq.heappush(minhq, int(num))
        else:
            if (num == "-1" and minhq):  # 최솟값 삭제
                item = heapq.heappop(minhq)
                maxhq.remove(-item)
            elif (num == "1" and maxhq):  # 최댓값 삭제
                item = heapq.heappop(maxhq)
                minhq.remove(-item)
    # 연산 끝
    return [-heapq.heappop(maxhq), heapq.heappop(minhq)] if minhq else [0,0]