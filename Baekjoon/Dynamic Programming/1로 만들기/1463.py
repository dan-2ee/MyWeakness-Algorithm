import sys
    
n = int(sys.stdin.readline())
cnt = 0

dp = [0, 0, 1, 1]
for i in range(4, n+1):
    dp.append(dp[i-1]+1)
    ''' dp[i]: 전 값에 1을 더해서 만들 수 있는 경우 
        dp[i//2]+1: 2로 나눠서 만들 수 있는 경우
        dp[i//3]+1: 3으로 나눠서 만들 수 있는 경우 '''
    if (i%2 == 0):
        dp[i] = min(dp[i], dp[i//2]+1)
    if (i%3 == 0):
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])