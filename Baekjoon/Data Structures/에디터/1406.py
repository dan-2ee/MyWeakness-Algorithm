import sys

input = sys.stdin.readline
leftWords = list(input().strip())
rightWords = []

T = int(input())

for _ in range(T):
    command = input().split()
    if (command[0] == "L" and leftWords):
        rightWords.append(leftWords.pop())
    elif (command[0] == "D" and rightWords):
        leftWords.append(rightWords.pop())
    elif (command[0] == "B" and leftWords):
        leftWords.pop()
    elif (command[0] == "P"):
        leftWords.append(command[1])
    
print("".join(leftWords)+ "".join(reversed(rightWords)))