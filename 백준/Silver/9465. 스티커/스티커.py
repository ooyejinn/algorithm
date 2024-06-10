T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    DP = [[0]*N for _ in range(2)]

    DP[0][0] = arr[0][0]
    DP[1][0] = arr[1][0]

    # N이 1 인 경우는 따로 고려해야 한다 (c-2를 고려할 수 없어진다)
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    DP[0][1] = max(arr[0][1], arr[1][0]+arr[0][1])
    DP[1][1] = max(arr[1][1], arr[0][0]+arr[1][1])

    for c in range(2, N):
        DP[0][c] = max(DP[1][c-1], DP[1][c-2]) + arr[0][c]
        DP[1][c] = max(DP[0][c-1], DP[0][c-2]) + arr[1][c]

    print(max(DP[0][N-1], DP[1][N-1]))