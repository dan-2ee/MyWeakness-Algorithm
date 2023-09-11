import sys

def countCandy(candy):
    cntCandy = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j-1] == candy[i][j]:
                cnt += 1
            else:
                cnt = 1
            cntCandy = max(cntCandy, cnt)
        cnt = 1
        for j in range(1, N):
            if candy[j-1][i] == candy[j][i]:
                cnt += 1
            else:
                cnt = 1
            cntCandy = max(cntCandy, cnt)
    return cntCandy

N = int(sys.stdin.readline())
candy = [list(sys.stdin.readline().strip()) for _ in range(N)]
maxCandy = 0

for i in range(N):
    for j in range(1, N): 
        candy[i][j-1], candy[i][j] = candy[i][j], candy[i][j-1]
        cnt = countCandy(candy)
        maxCandy = max(cnt, maxCandy)
        candy[i][j-1], candy[i][j] = candy[i][j], candy[i][j-1]   
    
    for j in range(1, N):
        candy[j-1][i], candy[j][i] = candy[j][i], candy[j-1][i]
        cnt = countCandy(candy)
        maxCandy = max(maxCandy, cnt)
        candy[j-1][i], candy[j][i] = candy[j][i], candy[j-1][i]

print(maxCandy)


