from collections import deque

def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0

    def bfs(idx):
        Q = deque()
        Q.append(idx)
        visited[idx] = 1
        
        while Q:
            c = Q.popleft()
            for next in range(n):
                if computers[c][next] == 1 and visited[next] == 0:
                    visited[next] = 1
                    Q.append(next)
                    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            bfs(i)
    
    return answer