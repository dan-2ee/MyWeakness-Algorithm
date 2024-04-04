s = input().strip()
tmp = []  # 현재 단어
answer = ""
isTag = 0  # 태그 안의 단어인지 
for alpha in s:
    if alpha==' ' and not isTag:  # 태그가 아닌 단어 입력이 끝났을 경우 
        answer+=''.join(tmp[::-1])+' '  # 뒤집고 띄어쓰기 추가
        tmp = []
    elif alpha=='<':
        isTag = 1
        answer+=''.join(tmp[::-1]) # 태그 열리기 이전 단어 붙임
        tmp=[]
    elif alpha=='>':
        isTag = 0 # 태그 끝남 
        answer+='<'+''.join(tmp)+'>' # 태그 안의 단어는 뒤집지 않음 
        tmp = []
    else:
        tmp.append(alpha)
if tmp: # 마지막 단어
    answer+=''.join(tmp[::-1])
print(answer)