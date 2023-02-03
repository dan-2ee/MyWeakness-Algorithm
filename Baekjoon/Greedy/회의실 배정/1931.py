import sys

n = int(sys.stdin.readline())
timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timeTable.sort(key = lambda x : (x[1], x[0]))   # 끝나는 시간이 빠른 순으로 정렬 

idx, isDone = 0, 0
cnt = 1
start = timeTable[0][1]

while (idx < n-1 and not isDone):
    for i in range(idx+1, n):
        if (timeTable[i][0] >= start):
            idx = i
            cnt += 1
            start = timeTable[i][1]
            continue
    # 다음 시간표 존재하지 않으면 끝냄 
    isDone = 1
print(cnt)