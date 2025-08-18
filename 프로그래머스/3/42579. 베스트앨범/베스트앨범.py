from collections import defaultdict

def solution(genres, plays):
    N = len(plays)
    genres_cnt = defaultdict(int)
    
    for i in range(N):
        genre = genres[i]
        play = plays[i]
        genres_cnt[genre] += play
        
    song_info = []
    
    for i in range(N):
        genre = genres[i]
        play = plays[i]
        
        song_info.append([-genres_cnt[genre], -play, i, genre])
        
    song_info.sort()
    
    genre_picked = defaultdict(int)
    answer = []
    
    for _, _, i, genre in song_info:
        if genre_picked[genre] < 2:
            answer.append(i)
            genre_picked[genre] += 1
            
    return answer