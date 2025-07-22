from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    
    for genre, play in zip(genres, plays):
        genre_total[genre] += play
        
    songs = []
    
    # 다시 순회하며, idx 붙여서 하나씩 봄...
    # 해당 장르 토탈 재생 수, (이후 sort 시 python은 오름차순이니 - 붙임)
    # 해당 곡 재생 수, (이후 sort 시 python은 오름차순이니 - 붙임)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs.append((-genre_total[genre], -play, idx, genre))
        
    songs.sort()
    
    # 이건 장르별 뽑은 곡 개수
    picked = defaultdict(int)
    answer = []
    
    for _, _, idx, genre in songs:
        if picked[genre] < 2:
            answer.append(idx)
            picked[genre] += 1
    
    return answer