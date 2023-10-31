def solution(elements):
    answer = set()
    N = len(elements)
    elements *= 2
    
    for i in range(N):
        for j in range(N):
            answer.add(sum(elements[j:i+j+1]))
    return len(answer)
        