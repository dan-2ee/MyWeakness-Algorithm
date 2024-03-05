from itertools import product

def solution(numbers, target):
    # 연산자 리스트: [+. -] 중에서 중복 포함 4개 뽑음
    operations = [item for item in product(['+', '-'], repeat=len(numbers))]  
    answer = 0
    for oper in operations:
        sum = 0
        for sign, num in zip(oper, numbers):
            # sign = + or -
            sum = sum + num if (sign == '+') else sum - num
        # 계산 결과가 target 일 경우 카운트 += 1
        if (sum == target):
            answer += 1
    
    return answer