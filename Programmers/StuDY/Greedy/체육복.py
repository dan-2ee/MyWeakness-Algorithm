def solution(n, lost, reserve):
    lostcnt = len(lost)
    lost.sort()
    for l in lost:
        if not reserve: break  # 빌려줄 수 있는 사람이 없는 경우
        if (l in reserve):    # 여분을 가져온 사람이 도난 당한 경우
            lostcnt -= 1
            reserve.remove(l)
        # 작은 번호부터 탐색 (다음 숫자도 받을 수 있도록)
        elif (l-1 in reserve and l-1 not in lost):
            lostcnt -= 1
            reserve.remove(l-1)
        elif (l+1 in reserve and l+1 not in lost):
            lostcnt -= 1
            reserve.remove(l+1)
    
    return n-lostcnt