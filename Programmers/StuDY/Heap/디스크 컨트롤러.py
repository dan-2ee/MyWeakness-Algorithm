import heapq 

def solution(jobs):
    takenTime, now = 0, -1
    answer, hq = [], []
    
    while (len(answer) < len(jobs)):
        # 끝난 시간 기준으로 전에 들어온 요청 hq 에 넣음
        for start, taken in jobs:
            if (now < start <= takenTime):
                # (소요 시간, 요청 시간)
                heapq.heappush(hq, (taken, start))
        
        if (hq):
            taken, start = heapq.heappop(hq)
            now = takenTime
            takenTime += taken
            answer.append(takenTime-start)
        else:
            # 끝난 시간 기준으로 전에 들어온 요청이 없으면 
            takenTime += 1
    return sum(answer) // len(answer)
            