# import heapq
# 시간 초과 
# def solution(n, times):
#     timetable = {time: 0 for time in range(len(times))}  
#     answer = 0
#     while (n > 0):  # 모든 사람이 끝날 때까지
#         hq = []
#         for i, time in enumerate(times):
#             if (timetable[i] == 0):  # 사용 중이 아님 
#                 heapq.heappush(hq, (time, i))
#             elif (timetable[i] != 0):   # 사용중
#                 heapq.heappush(hq, (timetable[i] + time, i))
                
#         time, idx = heapq.heappop(hq) 
#         timetable[idx] = time  # 제일 적은 시간으로 바꿈
#         n-=1
#     return max(timetable.values())

import heapq, sys

def solution(n, times):
    heapq.heapify(times)
    left, right = 1, max(times)*n   # 최소 시간, 최대 시간 
    answer = sys.maxsize
    while left <= right:
        people = 0
        mid = (left+right)//2
        for time in times:
            people += mid // time   # mid 시간동안 time 심사관이 몇 명 심사할수 있는지
            if (people >= n):
                # n명 이상 심사 했으면 break
                break
        if (people >= n):  
            answer = min(answer, mid)
            right = mid-1
        else:  # n명보다 적게 심사한 경우
            left = mid + 1

    return answer    