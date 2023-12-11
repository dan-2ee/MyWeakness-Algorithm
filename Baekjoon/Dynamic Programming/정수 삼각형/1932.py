import sys

input = sys.stdin.readline
N = int(input())
triangles = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*N
dp[0] = triangles[0][0]

for i in range(1, N):
    lst = []
    for j in range(i+1):
        if (j==0):  # 맨 왼쪽 
            lst.append(triangles[i][j]+dp[j])
        elif (j==i):   # 맨 오른쪽
            lst.append(triangles[i][j]+dp[j-1])
        else:  # 가운데 
            lst.append(triangles[i][j]+max(dp[j-1], dp[j]))
    dp[:i+1] = lst

print(max(dp))