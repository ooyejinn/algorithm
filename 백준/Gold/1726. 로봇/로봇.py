from collections import deque
#.    동, 서, 남, 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 인덱스, 튜플
# 동(0): 좌회전-북(3), 우회전-남(2)
# 이건 가는 방향에는 전혀 영향을 끼치지 않음
# 오직 회전방향 체크에만 쓰임
turn = [(3, 2), (2, 3), (0, 1), (1, 0)]

# 세로, 가로
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sr, sc, sd = map(int, input().split())
sr -= 1
sc -= 1
sd -= 1
er, ec, ed = map(int, input().split())
er -= 1
ec -= 1
ed -= 1

Q = deque()
visited = [[[0]*4 for _ in range(M)] for __ in range(N)]

Q.append((sr, sc, sd, 0))
while Q:
    cr, cc, cd, ccnt = Q.popleft()

    if cr == er and cc == ec and cd == ed:
        print(ccnt)
        break

    for d in range(2):
        nd = turn[cd][d]
        if visited[cr][cc][nd] == 0:
            visited[cr][cc][nd] = 1
            Q.append((cr, cc, nd, ccnt+1))

    # 전진
    for p in range(1, 4):
        nr = cr + dr[cd]*p
        nc = cc + dc[cd]*p

        # 경로를 진행하다 장애물 만나면
        if not (0<=nr<N and 0<=nc<M) or arr[nr][nc]==1:
            # break로 for문 탈출 (뒤의 range 돌지 않음)
            break

        else:
            if visited[nr][nc][cd] == 0:
                visited[nr][nc][cd] = 1
                Q.append((nr, nc, cd, ccnt+1))