import sys

def checkGroupWord(word):
    stack = []
    for i in word:
        if (i not in stack):
            stack.append(i)
        elif (stack[-1] == i):
            continue
        else:
            return 0
    return 1


t = int(sys.stdin.readline())
cnt = 0
for _ in range(t):
    word = sys.stdin.readline().strip()
    cnt += checkGroupWord(word)
print(cnt)