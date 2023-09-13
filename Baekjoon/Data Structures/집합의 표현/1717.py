import sys

def find(a):
    if (a != setlst[a]):
        setlst[a] = find(setlst[a])
    return setlst[a]

def union(a, b):
    x, y = find(a), find(b)
    setlst[y] = x

n, m = map(int, sys.stdin.readline().split())
setlst = [i for i in range(0, n+1)]  

for _ in range(m):
    order, a, b = map(int, sys.stdin.readline().split())
    if (order == 0):  
        union(a, b)
    else:  
        print("YES") if (find(a) == find(b)) else print("NO")
