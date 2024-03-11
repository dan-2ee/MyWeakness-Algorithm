def solution(nums):
    setnums = set(nums)
    if (len(setnums) <= len(nums)//2):  # 가져갈 수 있는 종류의 전부가 최대인 경우 
        return len(setnums)
    else:    # 전부 다 다른 종류를 가져가는 경우
        return len(nums)//2