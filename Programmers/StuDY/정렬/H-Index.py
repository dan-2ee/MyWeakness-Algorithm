def findSection(num, citations):
    for idx, i in enumerate(citations):
        # 기준 숫자 (num)보다 커지는 구간의 인덱스 리턴
        if (num <= i): return idx
        
def solution(citations):
    citations.sort()
    answer = 0
    for i in range(max(citations), -1, -1):
        idx = findSection(i, citations)
        # i번 이상 인용된 논문의 개수가 i편 이상인 경우 
        if (len(citations[idx:]) >= i):
            answer = max(answer, i)
    return answer