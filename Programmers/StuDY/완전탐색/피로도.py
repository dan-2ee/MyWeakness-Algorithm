from itertools import permutations

def countPassable(k, dungeons):
    # dungeons:  던전 리스트(방문 순서 정해짐)
    for item in dungeons:
        # 필요 피로도가 충분하지 않은 경우 or 탐험 후 피로도가 0보다 적은 경우
        if (item[0] > k or k - item[1] < 0):    
            return 0
        k -= item[1]   # 현재 피로도 - 소모 피로도
    # 탐험할 수 있는 경우, 던전 수 리턴
    return len(dungeons)

def solution(k, dungeons):
    answer = -1
    for i in range(1, len(dungeons)+1):
        for item in permutations(dungeons, i):
            answer = max(answer, countPassable(k, item))
            
    return answer