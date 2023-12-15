import sys

def solution(start):
    if (len(result) == M):
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, N+1):
        result.append(i)
        solution(i+1)
        result.pop()
    
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
solution(1)
