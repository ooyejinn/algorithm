from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]


def bfs():
    Q = deque()
    Q.append((0, 0, 0, 0))

    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while Q:
        sr, sc, scount, breaked = Q.popleft()
        if sr == N-1 and sc == M-1:
            return scount + 1

        for d in range(4):
            nr = sr+dr[d]
            nc = sc+dc[d]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 0 and not visited[nr][nc][breaked]:
                    visited[nr][nc][breaked] = 1
                    Q.append((nr, nc, scount+1, breaked))
                elif arr[nr][nc] == 1 and not breaked and not visited[nr][nc][1]:
                    visited[nr][nc][1] = 1
                    Q.append((nr, nc, scount+1, 1))

    return -1


print(bfs())