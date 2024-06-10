'''
1. 먼저 가능한 모든 나라의 국경선을 연다.
    1-1. 인접한 칸의 두 나라 간의 인구 차이가 (L <= 인구차이 <= R) 라면, 국경선을 연다.

2. 인구 이동을 진행한다.
    2-1. 각 연합 (국경선이 열려 일시적으로 합쳐진 나라들) 에서 인구 이동이 진행된다.
    2-2. 인구이동 후 각 국가의 인구 수는 (연합의 인구수 / 연합 국가수)가 된다.

3. 1-1의 조건을 충족하지 못하게 될 때까지 인구 이동을 반복한다.

4. 인구 이동이 며칠 동안 발생하는지 출력한다
'''
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def make_union(sr, sc):
    Q = deque()
    Q.append((sr, sc))
    now_union = [(sr, sc)]
    visited[sr][sc] = 1
    total_population = arr[sr][sc]
    countries_num = 1

    while Q:
        r, c = Q.popleft()

        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (L <= abs(arr[r][c] - arr[nr][nc]) <= R):
                visited[nr][nc] = 1
                Q.append((nr, nc))
                now_union.append((nr, nc))
                total_population += arr[nr][nc]
                countries_num += 1

    for ur, uc in now_union:
        arr[ur][uc] = total_population // countries_num

    # 연합이 2개 이상이면 True 반환해서 인구 이동시킴
    if countries_num >= 2:
        return True

    else:
        return False


def movement():
    global visited

    moved = False
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if make_union(r, c):
                    moved = True
    return moved


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

days = 0

while True:
    if not movement():
        break
    days += 1

movement()
print (days)