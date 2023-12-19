import sys

def backtracking(cnt):
    if (cnt == M):
        print(" ".join(map(str, lst)))
        return 
    duplicatedNum = 0
    for i in range(N):
        if (not visited[i] and duplicatedNum != nums[i]):
            duplicatedNum = nums[i]
            lst.append(nums[i])
            visited[i] = 1
            backtracking(cnt+1)
            visited[i] = 0
            lst.pop()


input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
visited = [0]*N
backtracking(0)