from collections import deque

# 토마토 같은 느낌으로 '한번에' 처리하고,
# 그렇게 딱 한 바퀴만 다 돈 뒤 (중요)
# += 1년,
# 그리고 이게 빙산 두 개로 분리 됐는지 확인

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

def melting():
    Q = deque()
    # 녹을 예정인 장소 미리 저장해서 한번에 녹이기
    melting = [[0]*M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                Q.append((r, c))

    while Q:
        cr, cc = Q.popleft()
        water_cnt = 0
        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                water_cnt += 1
        melting[cr][cc] = water_cnt

    for r in range(N):
        for c in range(M):
            arr[r][c] = max(0, arr[r][c] - melting[r][c])


def check_split():
    visited = [[0]*M for _ in range(N)]
    components = 0

    # 연결된거 다 확인
    def bfs(sr, sc):
        Q = deque([(sr, sc)])
        visited[sr][sc] = 1
        while Q:
            cr, cc = Q.popleft()
            for d in range(4):
                nr, nc = cr+dr[d], cc+dc[d]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] > 0:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
    
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and visited[r][c] == 0:
                components += 1
                if components > 1:
                    return True
                bfs(r, c)

    return False

def simulate():
    global result
    while True:
        melting()
        result += 1

        if check_split():
            return result

        # 맵 다 도는 동안 값이 싹다 0이면 0 리턴
        if all(arr[r][c] == 0 for r in range(N) for c in range(M)):
            return 0

print(simulate())
