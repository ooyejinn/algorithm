from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    def bfs(c):
        Q = deque()
        Q.append(c)
        
        while Q:
            now = Q.popleft()
            for i in range(n):
                if computers[now][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    Q.append(i)
        
        return
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            bfs(i)
    
    return answer