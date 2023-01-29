import sys

def findOrder(queue):
    order = 0
    while(1):
        findMax = max(queue, key = lambda x:x[0])
        if (queue[0][0] == findMax[0]):   # 맨 앞이 max 값이면 바로 pop
            order += 1
            item = queue.pop(0)
            if (item[1] == "True"):
                return order
        else:           # 맨 앞이 max 가 아니면 뒤로 다시 append 
            queue.append(queue.pop(0))

T = int(sys.stdin.readline())   
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        queue[i] = [queue[i], "True"] if (i == m) else [queue[i], "False"]
    
    print(findOrder(queue))
    