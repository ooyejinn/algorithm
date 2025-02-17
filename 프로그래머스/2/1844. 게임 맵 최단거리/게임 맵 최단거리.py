from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    Q = deque()
    Q.append((0, 0, 1))
    
    while Q:
        r, c, cnt = Q.popleft()
        if r == N-1 and c == M-1:
            return cnt
        
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and maps[nr][nc]==1:
                visited[nr][nc]=1
                Q.append((nr, nc, cnt+1))
    
    return -1