from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 불 시간 기록
    fireQ = deque()
    firetime = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if arr[r][c] == '*':
                fireQ.append((r, c))
                firetime[r][c] = 1

    while fireQ:
        cr, cc = fireQ.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 불이 갈 수 있는 곳인지
            if 0 <= nr < N and 0 <= nc < M and (arr[nr][nc] == '.' or arr[nr][nc] == '@'):
                # 퍼지는 불
                if firetime[nr][nc] == 0 or (firetime[nr][nc] != 0 and (firetime[nr][nc] > firetime[cr][cc] + 1)):
                    firetime[nr][nc] = firetime[cr][cc] + 1
                    fireQ.append((nr, nc))

    # 상근이
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '@':
                pr = r
                pc = c

    Q = deque()
    Q.append((1, pr, pc))
    visited = [[0] * M for _ in range(N)]
    visited[pr][pc] = 1

    flag = 0
    while Q:
        ct, cr, cc = Q.popleft()

        # 끝에 도착
        if cr == 0 or cr == N-1 or cc == 0 or cc == M-1:
            print(ct)
            flag = 1
            break

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 상근이가 갈 수 있는 곳인지
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == '.':
                # 상근이가 갈 수 있는 곳이 아직 불이 퍼지지 않은 곳인지
                if ct+1 < firetime[nr][nc] or (firetime[nr][nc] == 0):
                    Q.append((ct + 1, nr, nc))
                    visited[nr][nc] = 1


    if flag == 0:
        print('IMPOSSIBLE')