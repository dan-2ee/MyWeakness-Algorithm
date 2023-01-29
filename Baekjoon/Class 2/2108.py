import sys
from collections import Counter

n = int(sys.stdin.readline())  
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort() 

def average():
    return round(sum(numbers)/n)

def median():
    return numbers[n//2]

def mode():
    if (n == 1):
        return numbers[0]
    else:
        item = Counter(numbers).most_common()
        if (item[0][1] == item[1][1]):    
            return item[1][0]
        else:
            return item[0][0]

def range():
    return numbers[n-1] - numbers[0]

print((average()))
print(median())
print(mode())
print(range())