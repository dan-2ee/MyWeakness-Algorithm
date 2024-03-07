def solution(answers):
    routine = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = []  # 각 방식의 점수 리스트
    for idx in range(3):  
        nowRoutine = routine[idx]
        size = len(nowRoutine)
        # 점수 계산: answers 와 같으면 1 
        nowScore = sum(1 for i in range(len(answers)) if answers[i] == nowRoutine[i%size])
        score.append(nowScore)
    
    # 최대 스코어와 같은 사람 answer 배열에 추가
    maxScore = max(score)
    answer = [idx+1 for idx, item in enumerate(score) if (item == maxScore)]
                
    return answer