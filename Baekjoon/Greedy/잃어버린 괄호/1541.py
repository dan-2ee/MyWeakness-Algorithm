import sys
import re
def findMin():
    sum = int(lst[0])
    for i in range(1, len(lst)):
        if (lst[i].isdigit() and lst[i-1] == "-"):
            sum -= int(lst[i])
        elif (lst[i].isdigit() and lst[i-1] == "+"):
            sum += int(lst[i])
    return sum
            
        
str = sys.stdin.readline().strip()
idx = str.find("-")
newStr = str[:idx] + str[idx:].replace("+", "-")

lst = re.split('([+-])', newStr)
print(findMin())
