from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# '다른' 섬에 도달하는 것 때문에 이래저래 고민했는데,
# 전역 visited로 처리해서 이거저거 한번에 처리하기로 함 (같은 섬 + 가장자리 등 처리)
visited = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    # 다리 탐색할 Q (현재 섬에서 '아직 방문하지 않은' 새 섬으로)
    Q = deque()
    visited[r][c] = 1

    # 현재 섬 탐색하는 Q
    island_Q = deque([(r, c)])

    while island_Q:
        sr, sc = island_Q.popleft()
        for d in range(4):
            nr, nc = sr+dr[d], sc+dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    island_Q.append((nr, nc))
                # 새 좌표가 바다일 경우 = 현재 지점은 가장자리
                elif arr[nr][nc] == 0:
                    Q.append((nr, nc, 1))

    while Q:
        sr, sc, dist = Q.popleft()
        for d in range(4):
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                # '새 섬'에 도착했을 경우
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    return dist
                # '바다'일 경우 마저 탐색...
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 2
                    Q.append((nr, nc, dist + 1))

    return float('inf')


min_bridge = float('inf')

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            min_bridge = min(min_bridge, bfs(r, c))

print(min_bridge)