from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    N = len(words)
    visited = [0 for _ in range(N)]
    
    def is_connected(A, B):
        distance = 0
        
        for a, b in zip(A, B):
            if a != b:
                distance += 1
            
            if distance > 1:
                return False
        
        return distance == 1
        
    Q = deque()
    Q.append((begin, 0))
    
    while Q:
        cur_word, cur_cnt = Q.popleft()
        if cur_word == target:
            return cur_cnt
        
        for i in range(N):
            if visited[i] == 0 and is_connected(cur_word, words[i]):
                visited[i] = 1
                Q.append((words[i], cur_cnt+1))
    
    return 0