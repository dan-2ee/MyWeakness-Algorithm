def Backtracking(cnt):
    if (cnt == M):
        print(" ".join(map(str, lst)))
        return 
    for i in range(N):
        if (not visited[i]):
            lst.append(nums[i])
            visited[i] = 1
            Backtracking(cnt+1)
            visited[i] = 0
            lst.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
visited = [0] * N
Backtracking(0)
