from itertools import product
# 순서 있고, 중복 가능

def binarySearch(words, target):
    start, end = 0, len(words)
    while (start <= end):
        mid = (start + end)//2
        if (words[mid] == target):
            return mid+1  # mid는 인덱스이기 때문에 +1 해서 리턴
        elif (words[mid] > target):
            end = mid-1
        else:
            start = mid+1
            
        
def solution(word):
    words = []
    for size in range(1,6):
        for item in product(['A','E','I','O','U'],repeat=size):
            words.append(''.join(item))
    words.sort()
    return binarySearch(words, word)