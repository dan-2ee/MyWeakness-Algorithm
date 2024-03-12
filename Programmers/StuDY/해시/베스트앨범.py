def solution(genres, plays):
    musiclist = {genre:[] for genre in set(genres)}
    total = {genre:0 for genre in set(genres)} 
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # value = (재생횟수, 고유번호) 형태로 저장
        musiclist[genre].append((play, idx))
        total[genre] += play
    
    # 장르 배열 정렬 (총 재생횟수 기준) 
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for key, _ in total:
        # 장르별 재생횟수(내림차순), 고유번호(오름차순) 기준으로 정렬
        musiclist[key].sort(key = lambda x: (x[0], -x[1]), reverse=True)
        now = musiclist[key]
        if (len(now) == 1):
            answer.append(now[0][1])
        else:
            answer += [now[0][1], now[1][1]]
            
    return answer