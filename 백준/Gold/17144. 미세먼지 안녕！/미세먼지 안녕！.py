'''
T초 동안 아래의 일이 반복된다.
1. 미세먼지 확산
    1-1. 확산은 동시에 진행된다. (순차적 반영 X deepcopy O)
    1-2. 미세먼지가 있는 모든 칸에서 갈 수 있는 모든 방향으로 A/5만큼 확산된다. 소수점 버림.
        1-2-1. 값이 4 이하면 확산되지 않음
    1-3. A칸에 남은 미세먼지의 양은 A - (A/5)*(확산된 개수)
2. 공기청정기 작동 (공기청정기는 세로 2칸 차지)
    1-1. 공기청정기의 바람은 공기청정기가 위치한 칸에서 매번 상, 하 1개씩 총 2개 새로 생성된다.
    1-2. 윗칸은 반시계방향, 아래칸은 시계방향으로 회전한다.
    1-3. 바람의 방향대로 미세먼지가 한 칸씩 이동한다.
    1-4. 미세먼지가 공기청정기가 있는 칸에 도달하면 없어진다.

---

1. 공기청정기 위치 체크
2. 확산
    if arr[r][c] > 4:
        temp = arr[r][c]//5
        네 방향, arr 범위 내, 공기청정기 위치는 제외
            네 방향에 += temp
            arr[r][c] -= temp * (확산된 방향)
3. 순환 (x1: 청정기 윗칸 r 값)
    case1. [x1-1][0]에서부터 [0][0]까지 r이 1씩 감소하면서
        for i (x1-1, 0, -1)
            arr[i][0] <- arr[i-1][0]
    case2. [0][0]에서부터 [C-1][0]까지 c가 1씩 증가하면서
        for j (0, C-1, +1)
            arr[0][j] <- arr[0][j+1]
    case3. [0][C-1]에서부터 [x1][C-1]까지 r이 1씩 증가하면서
        for i (0, x1, 1)
            arr[i][C-1] <- arr[i+1][C-1]
    case4. [x1][1]에서부터 [x1][C-1]까지 c가 1씩 증가하면서
        for j (C-1, 0, -1)
            arr[x1][j] <- arr[x1][j-1]
'''
# from copy import deepcopy
# import sys
# sys.stdin = open('input.txt', 'r')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 청정기 위치 저장
# airfilter = []
for i in range(R):
    if arr[i][0] == -1:
        # airfilter.append((i, 0))
        # arr[i][0] = 0
        x1, x2 = i, i+1
        arr[x1][0] = arr[x2][0] = 0
        break


# T초간 반북
for _ in range(T):
    # 1. 확산
    # 동시에 확산되어야 하므로 전체 복사 후 한번에 처리해야 함
    # arr_t = deepcopy(arr)
    arr_t = [x[:] for x in arr] # deepcopy 안쓰고 일일히 하나하나 for문 돌려 복사

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 4:
                t = arr[i][j] // 5
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i+di, j+dj
                    # if 0<=ni<R and 0<=nj<C and (ni, nj) not in airfilter:
                    if 0<=ni<R and 0<=nj<C and (ni,nj) != (x1,0) and (ni,nj) != (x2,0):
                        arr_t[i][j] -= t
                        arr_t[ni][nj] += t
    arr = arr_t

    # 2. 순환
    # x1, x2 = airfilter[0][0], airfilter[1][0]

    # 윗칸
    for i in range(x1-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for j in range(0, C-1, 1):
        arr[0][j] = arr[0][j+1]
    for i in range(0, x1, 1):
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 0, -1):
        arr[x1][j] = arr[x1][j-1]

    # 아랫칸
    for i in range(x2+1, R-1, 1):
        arr[i][0] = arr[i+1][0]
    for j in range(0, C-1, 1):
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, x2, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 0, -1):
        arr[x2][j] = arr[x2][j-1]

ans = sum(map(sum, arr))
print(ans)