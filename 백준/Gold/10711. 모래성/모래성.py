from collections import deque

dr = [1, 1, 1, -1, -1, -1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, -1, 1]

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]


def sandcastle(N, M, arr):
    Q = deque()

    # 초기 상태 설정 및 모래가 없는 위치 큐에 추가
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '.':
                arr[r][c] = 0
                Q.append((r, c, 0))
            else:
                arr[r][c] = int(arr[r][c])

    max_time = 0
    while Q:
        r, c, time = Q.popleft()
        max_time = max(max_time, time)

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
                arr[nr][nc] -= 1
                if arr[nr][nc] == 0:
                    Q.append((nr, nc, time + 1))

    return max_time


print(sandcastle(N, M, arr))
