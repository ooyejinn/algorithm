from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0]*m for _ in range(n)]
    
    def bfs():
        Q = deque()
        Q.append((0, 0, 1))
        visited[0][0] = 1

        while Q:
            r, c, cnt = Q.popleft()

            if r == n-1 and c == m-1:
                return cnt

            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                    visited[nr][nc] =1
                    Q.append((nr, nc, cnt+1))
                    
        return -1
    
    return bfs()