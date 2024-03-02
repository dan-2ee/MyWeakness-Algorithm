import math

def solution(progresses, speeds):
    answer = []
    size = len(progresses)
    # 배포되기까지 걸리는 날짜 배열
    releaseDays = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)] 
    
    while(releaseDays):
        cnt = 1   # 배포되는 기능 개수
        stand = releaseDays[0]
        for day in releaseDays[1:]:
            if (stand >= day):
                cnt += 1
            else: 
                break
        answer.append(cnt)
        del releaseDays[:cnt]
    return answer