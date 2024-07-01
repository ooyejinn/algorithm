N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

DP = [[0]*3 for _ in range(N)]
DP[0][0] = costs[0][0]
DP[0][1] = costs[0][1]
DP[0][2] = costs[0][2]

for i in range(1, N):
    DP[i][0] = costs[i][0] + min(DP[i-1][1], DP[i-1][2])
    DP[i][1] = costs[i][1] + min(DP[i-1][0], DP[i-1][2])
    DP[i][2] = costs[i][2] + min(DP[i-1][0], DP[i-1][1])

print(min(DP[N-1][0], DP[N-1][1], DP[N-1][2]))