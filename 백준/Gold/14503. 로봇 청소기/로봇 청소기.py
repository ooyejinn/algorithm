dr = [-1, 0, 1, 0]  # 북 동 남 서
dc = [0, 1, 0, -1]  # 북 서 남 동
                    # 0 3 2 1
N, M = map(int, input().split())
sr, sc, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cr, cc, cd = sr, sc, sd
cnt = 0

while True: # 청소기가 더 이상 움직이지 못할 때 정료
    # 현재 칸에 청소 안 되어 있으면 청소
    if arr[cr][cc] == 0:
        arr[cr][cc] = 2
        cnt += 1
        
    flag = 1
    while flag == 1:
        # 반시계 방향 90도 회전 -> 앞쪽이 청소되지 않은 경우 한 칸 전진 후 1번
        for d in range(4):
            nd = (cd+3-d) % 4
            nr = cr+dr[nd]
            nc = cc+dc[nd]
            if arr[nr][nc] == 0:
                cr, cc, cd = nr, nc, nd
                flag = 0    # flag 0 + break로 인해 for문을 탈출하고 
                break       # 맨 위의 [cr][cc] == 0 을 체크하는 부분으로 감

        # 후진 (for문의 flag에 걸리지 않을 경우)
        else:
            nr = cr-dr[cd]
            nc = cc-dc[cd]
            if arr[nr][nc] == 1:
                print(cnt)
                exit()
            else:
                cr, cc = nr, nc

