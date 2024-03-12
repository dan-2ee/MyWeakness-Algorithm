import math
    
def solution(clothes):
    dic = {}
    for _, category in clothes:
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
    answer = 1
    # dic = {'headgear': 2, 'eyewear': 1}
    for value in dic.values():
        # value 개 중에서 0개 선택하거나, 1개를 선택하는 경우의 수 
        answer *= sum(math.comb(value, i) for i in range(2))
    # 최소 한개는 착용해야하므로, 모든 카테고리에서 선택하지 않는 경우 제외 
    return answer-1