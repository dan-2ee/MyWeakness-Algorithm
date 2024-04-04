s = input()
stack = []
answer = 0
tmp = 1
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] != '(':  # 괄호의 짝이 맞지 않을 경우 
            answer = 0
            break
        if s[i-1] == '(':  # () 인 경우 더해줌 
            answer += tmp
        stack.pop()
        tmp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if s[i-1] == '[':  # []인 경우 더해줌 
            answer += tmp
        stack.pop()
        tmp //= 3
if stack:  # 괄호의 짝이 맞지 않는 경우
    print(0)
else:
    print(answer)




