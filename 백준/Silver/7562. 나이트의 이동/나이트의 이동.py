from collections import deque

def bfs(sr, sc):
    Q = deque([(sr, sc, 0)])
    visited = [[-1]*(N) for _ in range(N)]
    visited[sr][sc] = 1

    while Q:
        r, c, cnt = Q.popleft()

        if r == er and c == ec:
            return cnt

        for d in [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)]:
            nr, nc = r+d[0], c+d[1]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                visited[nr][nc] = 1
                Q.append((nr, nc, cnt + 1))

T = int(input())

for tc in range(T):
    N = int(input())

    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    print(bfs(sr, sc))