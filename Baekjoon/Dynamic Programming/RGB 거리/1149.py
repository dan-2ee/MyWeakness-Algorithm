import sys

N = int(sys.stdin.readline())
dp = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]    # i번째 집을 빨간색으로 칠했을 때 드는 최소 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]    # i번째 집을 초록색으로 칠했을 때 드는 최소 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]    # i번째 집을 파란색으로 칠했을 때 드는 최소 비용

print(min(dp[N-1]))