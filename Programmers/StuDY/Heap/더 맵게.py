import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while (scoville[0] < K):
        if (len(scoville) < 2): return -1  # 원소 개수가 2개 이하이면 섞을 수 없음
        mixnum = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        answer += 1
        heapq.heappush(scoville, mixnum)
    return answer