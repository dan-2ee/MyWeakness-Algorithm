import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    num = int(sys.stdin.readline())
    stack.append(num) if (num) else stack.pop()

print(sum(stack))