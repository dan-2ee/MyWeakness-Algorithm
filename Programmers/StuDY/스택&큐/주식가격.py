def solution(prices):
    size = len(prices)
    answer = [0 for _ in range(size)]
    
    for i in range(size-1):
        for j in range(i+1, size):
            answer[i] += 1
            if (prices[i] > prices[j]):
                break
    
    return answer