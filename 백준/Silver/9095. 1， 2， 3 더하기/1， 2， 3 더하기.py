import sys
input = sys.stdin.readline

DP = [0] * 12
DP[1:4] = [1, 2, 4]

for i in range(4, 12):
    DP[i] = sum(DP[i-3:i])

T = int(input())
for _ in range(T):
    N = int(input())

    print(DP[N])