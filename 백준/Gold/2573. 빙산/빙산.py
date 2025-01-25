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
    # 빙산 개수 카운트
    ice_cnt = 0
    # 녹을 위치 및 양 저장
    melting = [[0] * M for _ in range(N)]
    # 빙산 위치 저장
    ice_positions = []

    # 빙산 위치 저장 + 녹을 양 개산
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                ice_cnt += 1
                ice_positions.append((r, c))
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                        melting[r][c] += 1
                        
    for r, c in ice_positions:
        arr[r][c] = max(0, arr[r][c] - melting[r][c])
        if arr[r][c] == 0:
            ice_cnt -= 1

    return ice_cnt


def check_split(ice_cnt):
    if ice_cnt == 0:
        return False

    visited = [[0]*M for _ in range(N)]

    # (r, c) for r in range(N) for c in range(M)
    # 2차원 배열의 모든 위치(r, c) 생성하는 제너레이터 표현식
    # if arr[r][c] > 0: 조건
    # next(...): 제너레이터에서 조건 만족하는 첫 항목 반환
    sr, sc = next((r, c) for r in range(N) for c in range(M) if arr[r][c] > 0)

    Q = deque([(sr, sc)])
    visited[sr][sc] = 1
    cnt = 1

    while Q:
        cr, cc = Q.popleft()
        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and arr[nr][nc]>0:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                cnt += 1

    # 이렇게 한 빙산(연결된) 개수가 전체 빙산 개개의 갯수랑 다르면 return
    return cnt != ice_cnt


def simulate():
    years = 0
    ice_cnt = sum(sum(row) > 0 for row in arr)

    while ice_cnt > 0:
        ice_cnt = melting()  # 빙산 녹이기 및 개수 갱신
        years += 1

        if check_split(ice_cnt):
            return years
    return 0


print(simulate())