import sys

stack = []
result = []
pushNum = 0   # 가장 최근에 push 한 숫자 저장 

def push(x):
    stack.append(x)
    result.append("+")

def pop():
    result.append("-")
    return (stack.pop())

n = int(sys.stdin.readline())   # 순열 갯수
numLst = [int(sys.stdin.readline()) for _ in range(n)]    # 순열

for num in numLst: 
    if (num < pushNum):
        if (pop() != num):
            result = ["NO"]                
            break
    else:
        while (pushNum != num):
            pushNum +=1
            push(pushNum)
        pop()

for i in result:
    print(i)