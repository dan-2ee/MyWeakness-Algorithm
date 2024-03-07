def solution(sizes):
    # w: 너비가 될 수 있는 값들중 큰 값
    # h: 작은 값
    w, h = [], []
    for wigth, height in sizes:
        w.append(max(wigth, height))
        h.append(min(wigth, height))
        
    return max(w) * max(h)