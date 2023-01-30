import sys

def sliceLine(start, end, needCnt, lines):
    L = (start + end) // 2
    if (start > end):
        return L
    lineCnt = 0
    for i in lines:
        lineCnt += (i//L)
    
    if (lineCnt >= needCnt):   # 필요한 개수보다 더 많이 만들 수 있는 경우 
        return sliceLine(L+1, end, needCnt, lines)    # 랜선 길이를 늘림 
    else:                  # 개수가 부족한 경우
        return sliceLine(start, L-1, needCnt, lines)   # 랜선 길이를 줄임 

k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]
print(sliceLine(1, max(lines), n, lines))

