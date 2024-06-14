import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] + [int(input().strip()) for _ in range(N)]

DP = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1):
    DP[i][0] = max(DP[i-1][1], DP[i-1][2])  # 안 밟기      : DP[i][1], DP[i][2] 중 큰 값
    DP[i][1] = DP[i-1][0] + arr[i]          # 1번 연속 밟기 : 0번 연속 밟기 + 지금 밟는 값
    DP[i][2] = DP[i-1][1] + arr[i]          # 2번 연속 밟기 : 1번 연속 밟기 + 지금 밟는 값

print(max(DP[N][1], DP[N][2]))