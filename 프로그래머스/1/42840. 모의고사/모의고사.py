def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # p[i % len(p)] : p의 인덱스 초과해도 계속 반복할 수 있도록
    scores = [sum(answers[i] == p[i % len(p)] for i in range(len(answers))) for p in patterns]
    
    max_score = max(scores)
    
    return [i + 1 for i, score in enumerate(scores) if score == max_score]