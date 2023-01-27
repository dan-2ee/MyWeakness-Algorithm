import sys
from collections import deque

def isBalance(str):
    bracket = ["(", ")", "[", "]"]
    # dq: 문자열에 포함된 괄호 저장
    # stack: dq 안의 괄호들 중 왼쪽 괄호들만 저장 
    dq = deque(word for word in str if (word in bracket))
    stack = []
    while (dq):
        item = dq.popleft()
        if (item == "(" or item == "["):   
            stack.append(item)
        else:    
            if not (stack):
                return "no"         
            else:
                leftBracket = stack.pop()
                if (leftBracket == "(" and item == "]"):
                    return "no"
                elif (leftBracket == "[" and item == ")"):
                    return "no"
    
    return ("no" if(stack) else "yes")

while 1:
    str = sys.stdin.readline().rstrip()
    if (str=="."):
        break
    else:
        print(isBalance(str))
