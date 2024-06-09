'''
출력해야 할 것

1. 치즈를 모두 녹이는데 걸리는 시간
2. 모두 녹기 한 시간 전 남아있는 치즈조각의 개수

---

0 : 공기
1 : 치즈
2 : 이번 cnt에 녹일 치즈

cnt += 1 한 뒤 Q 진행

while Q:
    범위 내 도달 가능한 1이 있다면 2로 만든다
    범위 내 도달 가능한 1이 없다면 해당 Q 종료 (0, 2밖에 없는 경우)
    
만약 1이 남아있지 않다면
    cnt, 2의 개수 출력

1이 남아있다면
    2를 0으로 바꾼 뒤 Q 진행
'''
from copy import deepcopy
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def melting(now_arr):
    Q = deque([(0, 0)])
    visited = [[0]*M for _ in range(N)]

    while Q:
        r, c = Q.popleft()

        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
                if now_arr[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                elif now_arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    now_arr[nr][nc] = 2

    return now_arr


def count(now_arr):
    return sum(row.count(1) for row in arr)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
last = 0


while True:

    # 만약 녹일 치즈 없으면 break
    cnt = count(arr)
    if cnt == 0:
        break

    last = cnt
    arr = melting(deepcopy(arr))

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                arr[r][c] = 0

    time += 1

print(time)
print(last)