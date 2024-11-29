dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# def findconnect(r, c):
#     print(f"Connecting ({r}, {c})")
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if mp[nr][nc] == 1 and visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 findconnect(nr, nc)


# def findconnect(r, c):
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0<=nr<N and 0<=nc<N:
#             if mp[nr][nc] == 1 and visited[nr][nc] == 0:
#                     visited[nr][nc] = 1
#                     findconnect(nr, nc)

# def findconnect(r, c):
#     visited[r][c] = 1
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if mp[nr][nc] == 1 and visited[nr][nc] == 0:
#                 findconnect(nr, nc)

def findconnect(r, c):
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if mp[nr][nc] == 1 and visited[nr][nc] == 0:
                    stack.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    # 가로, 세로, 배추 수
    # cabbage = [0] * K
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    mp = [[0]*M for _ in range(N)]

    for i in range(K):
        c, r = map(int, input().split())
        mp[r][c] = 1

    for r in range(N):
        for c in range(M):
            if mp[r][c] == 1 and visited[r][c] == 0:
                # visited[r][c] = 1
                cnt += 1
                findconnect(r, c)

    print(cnt)