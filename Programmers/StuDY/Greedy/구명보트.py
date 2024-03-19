def solution(people, limit):
    # 가벼운 순으로 정렬
    people.sort()
    left, right = 0, len(people)-1
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
             
    return answer
