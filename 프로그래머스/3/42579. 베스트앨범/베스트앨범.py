from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    N = len(plays)
    genres_cnt = defaultdict(int)
    
    for i in range(N):
        g = genres[i]
        p = plays[i]
        genres_cnt[g] += p
    
    song_info = []
    
    for i in range(N):
        g = genres[i]
        p = plays[i]
        # 원래 sort 하면 낮은 수 부터인데,
        # 높은 수부터 해야할 경우 - 붙이면 간단
        song_info.append([-genres_cnt[g], -p, i, g])
        
    song_info.sort()
    
    genres_picked = defaultdict(int)
    
    for _, _, i, g in song_info:
        if genres_picked[g] < 2:
            answer.append(i)
            genres_picked[g] += 1
    
    return answer