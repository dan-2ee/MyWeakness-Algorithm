def solution(number, k):
    stack = []
    for num in number:
        while (stack and stack[-1] < num and k > 0):
            stack.pop()
            k -= 1
        stack.append(num)
    if (k > 0):   # 제거해야할 개수가 남은 경우, 뒷부분 제거
        return ''.join(stack[:len(stack)-k])
    return ''.join(stack)