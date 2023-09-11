import sys

words = list(sys.stdin.readline().strip())
ans, stack = [], []
hasTag = 0
    
for w in words:
    if (w == " "):
        while (stack):
            ans.append(stack.pop())
        ans.append(" ")
    elif (w == "<"):
        while (stack):
            ans.append(stack.pop())
        ans.append("<")
        hasTag = 1
    elif (w == ">"):
        ans.append(">")
        hasTag = 0
    elif (hasTag):
        ans.append(w)
    else:
        stack.append(w)

    
while(stack):
    ans.append(stack.pop())
print("".join(ans))