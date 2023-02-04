import sys

def countMaxPeople():
    if (n == 1):
        return 1
    cnt = 1
    currentScore = scores[0][1]   # 2차 점수 기준으로 비교 

    for i in range(1, n):
        if (scores[i][1] < currentScore):
            cnt += 1
            currentScore = scores[i][1]
    return cnt

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    scores = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    scores.sort(key = lambda x: (x[0], x[1]))
    print(countMaxPeople())