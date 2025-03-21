from collections import deque

def solution(maps):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    N = len(maps)
    M = len(maps[0])
    visited = [[0]*M for _ in range(N)]
    
    Q = deque()
    Q.append((0, 0, 1))
    visited[0][0] = 1
    
    while Q:
        cr, cc, ccnt = Q.popleft()
        
        if cr == N-1 and cc == M-1:
            return ccnt
        
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = 1
                Q.append((nr, nc, ccnt+1))
    
    return -1