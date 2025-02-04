from collections import deque

def solution(begin, target, words):
    # 문제 조건에서 begin != target 은 이미 명시되어 있음
    if target not in words:
        return 0
    
    def is_connected(A, B):
        distance = 0
        
        for a, b in zip(A, B):
            if a != b:
                distance += 1
        
            if distance > 1:
                return False
        
        return distance == 1
    
    Q = deque([(begin, 0)])
    visited = [0] * len(words)
    
    while Q:
        c_word, cnt = Q.popleft()
        
        if c_word == target:
            return cnt
        
        for i in range(len(words)):
            if visited[i] == 0 and is_connected(c_word, words[i]):
                visited[i] = 1
                Q.append((words[i], cnt+1))
    
    return 0