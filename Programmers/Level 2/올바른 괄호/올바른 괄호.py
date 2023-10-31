def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append("(")
        else:    
            if not stack:
                return False
            else:
                stack.pop()
    return stack == []