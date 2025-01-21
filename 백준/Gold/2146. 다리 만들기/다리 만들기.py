from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = deque()
    visited[r][c] = 1

    island_Q = deque([(r, c)])

    while island_Q:
        sr, sc = island_Q.popleft()
        for d in range(4):
            nr, nc = sr+dr[d], sc+dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    island_Q.append((nr, nc))
                elif arr[nr][nc] == 0:
                    Q.append((nr, nc, 1))  # 바다에 인접한 지점부터 거리 1로 시작

    while Q:
        sr, sc, dist = Q.popleft()
        for d in range(4):
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    return dist
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 2
                    Q.append((nr, nc, dist+1))

    return float('inf')

min_bridge = float('inf')

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            min_bridge = min(min_bridge, bfs(r, c))

print(min_bridge)
