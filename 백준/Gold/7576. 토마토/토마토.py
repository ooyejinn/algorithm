from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
cnt = -1

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            Q.append((r, c))

while Q:
    # 아래 줄을 추가해주면 Q들 각각을 한번에 진행 가능!!! (몰랏다)
    for _ in range(len(Q)):
        cr, cc = Q.popleft()
        for d in range(4):
            nr = cr+dr[d]
            nc = cc+dc[d]
            if 0<=nr<N and 0<=nc<M and (arr[nr][nc] == 0):
                arr[nr][nc] = 1
                Q.append((nr, nc))
    cnt += 1

# 이걸로 안 익은 토마토 있는지 확인 가능
# -1 의 경우 원래부터 비어있는 줄이니 ㄴㄴ
# 0 만 토마토인데 안 익은 것
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            cnt = -1
            break
    if cnt == -1:
        break

print(cnt)