import sys

def sliceTree(start, end, target, tree):
    H = (start + end) // 2    # H: 중간값, 중간값으로 나무를 자름 
    take = 0   # 잘라서 가져갈 나무의 길이합
    for i in tree:
        if (H < i):
            take += (i - H)
    if (start > end or take == target):
        return H
    elif (take > target):    # 너무 많이 잘랐으면 H를 키움 
        return sliceTree(H+1, end, target, tree)
    else:                   # 너무 조금 잘랐으면 H를 낮춤 
        return sliceTree(start, H-1, target, tree)

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()
print(sliceTree(0, tree[n-1], m, tree))   # 인덱스가 아니라 길이를 전달함 