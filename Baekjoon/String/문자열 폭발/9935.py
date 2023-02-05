import sys

str = sys.stdin.readline().strip()
explode = sys.stdin.readline().strip()
stack = []
n = len(explode)

for i in str:
    stack.append(i)
    if (stack[-1] == explode[-1]):
        #if ("".join(stack[len(stack)-len(explode):]) == explode):
            #del stack[len(stack) - len(explode):]
        if ("".join(stack[-n:]) == explode):
            del stack[-n:]

new = "".join(stack)
print(new) if (new) else print("FRULA")
