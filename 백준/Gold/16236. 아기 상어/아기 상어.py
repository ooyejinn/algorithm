from collections import deque

def bfs(sr, sc):
    Q = deque()
    visited = [[0]*N for _ in range(N)]
    short_lst = []
    min_dist = float('inf')  # 최단 거리 초기화

    Q.append((sr, sc))
    visited[sr][sc] = 1

    while Q:
        cr, cc = Q.popleft()

        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and shark>=arr[nr][nc]:
                visited[nr][nc] = visited[cr][cc]+1
                if shark > arr[nr][nc] > 0:  # 먹을 수 있는 물고기라면
                    dist = visited[nr][nc] - 1  # 거리 계산
                    if dist < min_dist:  # 더 짧은 거리를 찾으면 리스트 초기화
                        short_lst = [(nr, nc)]
                        min_dist = dist
                    elif dist == min_dist:  # 같은 거리의 물고기 추가
                        short_lst.append((nr, nc))
                Q.append((nr, nc))

    # 가장 가까운 물고기들의 리스트와 그 거리를 반환
    return short_lst, min_dist

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

shark = 2
dinner = 0
cnt = 0

# 아기상어 위치 찾기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            cr, cc = r, c
            arr[r][c] = 0  # 아기 상어 위치 초기화

while True:
    short_lst, dist = bfs(cr, cc)
    if not short_lst:  # 먹을 물고기가 더 없다면
        print(cnt)
        break
    # 먹을 물고기 있는 경우
    short_lst.sort(key=lambda x: (x[0], x[1]))  # 행 우선으로 정렬
    cr, cc = short_lst[0]
    arr[cr][cc] = 0
    dinner += 1
    cnt += dist

    # shark 크기만큼 dinner 먹었을 경우
    if shark == dinner:
        shark += 1
        dinner = 0
