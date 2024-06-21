N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0]*3 for _ in range(N)] for _ in range(N)]
DP[0][1][0] = 1

for r in range(N):
    for c in range(1, N):
        # 장애물이 없다면
        if arr[r][c] == 0:
            # 가로, 세로의 경우 [r][c]만 비어있으면 됨
            DP[r][c][0] += DP[r][c-1][0] + DP[r][c-1][2]
            # 세로의 경우 r >= 1에만 있을 수 있음
            if r > 0:
                DP[r][c][1] += DP[r-1][c][1] + DP[r-1][c][2]
            # 대각선의 경우 [r-1][c], [r][c-1]또한 비어있어야 함
            # 대각선의 경우 r >= 1에만 있을 수 있음
            if r > 0 and arr[r-1][c] == 0 and arr[r][c-1] == 0:
                DP[r][c][2] += DP[r-1][c-1][0] + DP[r-1][c-1][1] + DP[r-1][c-1][2]

print(sum(DP[N-1][N-1]))