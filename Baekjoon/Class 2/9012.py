import sys

def isVPS(str):
    stack = []
    for i in str:
        if (i == "("):
            stack.append("(")
        else:
            if (stack): 
                stack.pop()
            else:
                return "NO"

    return ("NO" if (stack) else "YES")   
   
n = int(sys.stdin.readline())

for _ in range(n):
    str = sys.stdin.readline().strip()
    print(isVPS(str))