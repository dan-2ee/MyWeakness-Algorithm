import sys
        
lst = list(sys.stdin.readline().strip())
result, cnt, n = 0, 1, len(lst)
stack = []
for i in range(n):
    if (lst[i] == "("):
        stack.append("(")
        cnt *= 2
    elif (lst[i] == "["):
        stack.append("[")
        cnt *= 3
    elif (lst[i] == ")"):
        if (not stack or stack[-1] != "("):
            result = 0
            break
        elif (lst[i-1] == "("):
            result += cnt
        stack.pop()
        cnt //= 2
    else:
        if (not stack or stack[-1] != "["):
            result = 0
            break
        elif (lst[i-1] == "["):
            result += cnt
        stack.pop()
        cnt //= 3

print(0) if (stack) else print(result)