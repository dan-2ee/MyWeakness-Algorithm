from collections import Counter

def solution(k, tangerine):
    tangerineCount = Counter(tangerine)
    answer = 0
    for size, count in sorted(tangerineCount.items(), key = lambda x:x[1], reverse=True):
        k -= count
        answer += 1
        if k <=0:
            break
        
    return answer