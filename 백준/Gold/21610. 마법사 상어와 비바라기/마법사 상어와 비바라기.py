dr = [0,  0, -1, -1, -1,  0,  1,  1,  1]
dc = [0, -1, -1,  0,  1,  1,  1,  0, -1]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cmds = [tuple(map(int, input().split())) for _ in range(M)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in cmds:
    s %= N

    moved = []
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        moved.append((nr, nc))

    had_cloud = [[False] * N for _ in range(N)]
    for r, c in moved:
        A[r][c] += 1
        had_cloud[r][c] = True

    for r, c in moved:
        add = 0
        for drd, dcd in diag:
            rr, cc = r + drd, c + dcd
            if 0 <= rr < N and 0 <= cc < N and A[rr][cc] > 0:
                add += 1
        A[r][c] += add

    clouds = []
    for r in range(N):
        for c in range(N):
            if not had_cloud[r][c] and A[r][c] >= 2:
                A[r][c] -= 2
                clouds.append((r, c))

print(sum(map(sum, A)))
