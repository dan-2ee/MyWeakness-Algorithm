from itertools import permutations

def isPrime(num):
    # 소수인지 확인
    if (num <= 1): return 0
    for i in range(2, num//2+1):
        if (num%i == 0): return 0
    return 1
    
def solution(numbers):
    answer = 0
    able = set() # 가능한 숫자 모음
    for i in range(1, len(numbers)+1):  
        for item in permutations(numbers, i):
            able.add(int(''.join(item)))
            
    for num in able:
        answer += isPrime(num) # 소수이면 1을 더하고, 소수가 아니면 0을 더함 
    
    return answer