import sys

dp = [[0 for col in range(15)] for row in range(15)]    # 인덱스 1부터 사용


def countPeople(k, n):
    if (k == 1):
        return n*(n+1)//2   # 1부터 n까지의 합
    else:
        sum = 0
        count = 1
        while (count <= n):
            if (dp[k-1][count]):
                sum += dp[k-1][count]
            else:
                dp[k-1][count] = countPeople(k-1, count)
                sum += dp[k-1][count]
            count += 1
        return sum


T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(countPeople(k, n))
