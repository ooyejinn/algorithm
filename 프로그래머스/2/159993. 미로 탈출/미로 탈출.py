from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    
    def find(sr, sc):
        flag = 0
        cnt = 0
        visited = [[0 for _ in range(m)] for _ in range(n)]
        Q = deque()
        Q.append((sr, sc, cnt, flag, visited))
        
        while Q:
            cr, cc, ccnt, cflag, cvisited = Q.popleft()
            
            if cflag == 0:
                for d in range(4):
                    nr = cr+dr[d]
                    nc = cc+dc[d]
                    if 0<=nr<n and 0<=nc<m and not cvisited[nr][nc]:
                        cvisited[nr][nc] = 1
                        
                        if maps[nr][nc] == "L":
                            Q.append((nr, nc, ccnt+1, 1, cvisited))
                        elif maps[nr][nc] in ("O", "S", "E"):
                            Q.append((nr, nc, ccnt+1, 0, cvisited))
                            
            elif cflag == 1:
                for d in range(4):
                    nr = cr+dr[d]
                    nc = cc+dc[d]
                    if 0<=nr<n and 0<=nc<m and (cvisited[nr][nc] in (0, 1)):
                        cvisited[nr][nc] = 2
                        
                        if maps[nr][nc] == "S":
                            Q.append((nr, nc, ccnt+1, 1, cvisited))
                        elif maps[nr][nc] == "O":
                            Q.append((nr, nc, ccnt+1, 1, cvisited))
                        elif maps[nr][nc] == "E":
                            return ccnt+1
                
    for r in range(n):
        for c in range(m):
            if maps[r][c] == "S":
                return find(r, c) or -1