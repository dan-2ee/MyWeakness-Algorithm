N, M = map(int, input().split())
lst = []

def BackTracking(start, cnt):
    if (cnt - 1 == M):
        print(" ".join(map(str, lst)))
        return 
    
    for i in range(start, N+1):
        lst.append(i)
        BackTracking(i, cnt + 1)
        lst.pop()

BackTracking(1, 1)