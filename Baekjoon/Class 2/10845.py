import sys

queue = []

def size():
    return len(queue)

def empty():
    return (0 if (size()) else 1)

def push(x):
    queue.append(x)

def pop():
    print(-1) if (empty()) else print(queue.pop(0))

def front():
    print(-1) if (empty()) else print(queue[0])

def back():
    print(-1) if (empty()) else print(queue[-1])

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
    elif (command[0] == "front"):
        front()
    else:
        back()
