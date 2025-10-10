from collections import defaultdict

def solution(genres, plays):
    # 장르 별 두개씩
    # 1. 장르 합산 높은 장르부터 (모든 장르는 횟수 다름)
    # 2. 장르 내에서 더 많이 재생된 노래
    # 3. 장르 내 횟수 같을 시 고유번호 낮은 노래
    
    N = len(plays)
    genres_cnt = defaultdict(int)
    # {'pop': [(재생횟수, 고유번호), ()]}
    
    for i in range(N):
        g = genres[i]
        p = plays[i]
        
        genres_cnt[g] += p
        
    song_info = []
    
    for i in range(N):
        g = genres[i]
        p = plays[i]
        
        #                 -genres_cnt: 이렇게 하면 자동으로 높은 순서부터
        song_info.append([-genres_cnt[g], -p, i, g])
        
    song_info.sort()
    
    genre_picked = defaultdict(int)    
    answer = []
    
    for _, _, i, g in song_info:
        if genre_picked[g] < 2:
            answer.append(i)
            genre_picked[g] += 1
    
    return answer