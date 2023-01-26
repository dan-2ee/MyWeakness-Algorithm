import sys

deque = []

def size():
    return len(deque)

def empty():
    return (0 if (deque) else 1)

def push_front(x):
    deque.insert(0, x)

def push_back(x):
    deque.append(x)

def pop_front():
    print(-1) if (empty()) else print(deque.pop(0))

def pop_back():
    print(-1) if (empty()) else print(deque.pop())

def front():
    print(-1) if (empty()) else print(deque[0])

def back():
    print(-1) if (empty()) else print(deque[-1])

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if (command[0] == "push_front"):
        push_front(command[1])
    elif (command[0] == "push_back"):
        push_back(command[1])
    elif (command[0] == "pop_front"):
        pop_front()
    elif (command[0] == "pop_back"):
        pop_back()
    elif (command[0] == "size"):
        print(size())
    elif (command[0] == "empty"):
        print(empty())
    elif (command[0] == "front"):
        front()
    else:
        back()