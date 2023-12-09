import sys

def postorder(tree):
    if (not tree):
        return
    root = tree[0]
    leftTree, rightTree = [], []
    for i in range(1, len(tree)):
        if (tree[i] > root):
            leftTree, rightTree = tree[1:i], tree[i:]
            break
    else:
        leftTree = tree[1:]
    postorder(leftTree)
    postorder(rightTree)
    print(root)

sys.setrecursionlimit(10**6)
tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break
postorder(tree)