import sys

stack = []

def size():
    return len(stack)

def empty():
    return (0 if (size()) else 1)

def push(x):
    stack.append(x)

def pop():
    print(stack.pop(-1)) if (size()) else print(-1)

def top():
    print(-1) if (empty()) else print(stack[-1])

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    if (command[0] == "push"):
        push(command[1])
    elif (command[0] == "pop"):
        pop()
    elif (command[0] == "size"):
        print(size())
    elif (command[0] == "empty"):
        print(empty())
    else:
        top()