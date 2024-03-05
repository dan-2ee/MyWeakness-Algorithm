import sys

def compareWords(a, b):
    cnt = 0 # 다른 문자의 개수
    for i, j in zip(a, b):
        if (i != j):
            cnt += 1
            if (cnt > 1): 
                return 0  
    # 다른 문자의 개수가 1개 이하인 경우 = true
    return 1

def dfs(node, cnt, target, words):
    # node = 문자열의 인덱스
    global matrix, visited, answer
    if (words[node] == target):  # target이 된 경우
        answer = min(answer, cnt)
        return
    visited[node] = 1
    
    for idx, item in enumerate(matrix[node]):
        if (not visited[idx] and item): # 방문하지 않았고 교환 가능한 단어인 경우
            dfs(idx, cnt+1, target, words)
            visited[idx] = 0    # 다른 노드에서 재방문 가능하도록 visited=0으로 바꿈
        
def solution(begin, target, words):
    global matrix, visited, answer
    # 반환할 수 없는 경우 
    if (target not in words): return 0
    # begin 에서 바꿀 수 있는 단어 리스트 (인덱스)
    startWords = [idx for idx, word in enumerate(words) if compareWords(begin, word)]
    # 단어 리스트 길이 
    size = len(words)
    # 단어들간 교환 가능 여부
    matrix = [[0]*len(words) for _ in range(len(words))]
    for i in range(size):
        for j in range(i, size):
            matrix[i][j] = matrix[j][i] = compareWords(words[i], words[j])
    
    answer = sys.maxsize
    while (startWords):
        visited = [0]*size
        start = startWords.pop(0)
        dfs(start, 1, target, words)
        
    return answer