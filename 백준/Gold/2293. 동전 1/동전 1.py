# N가지, K원 만들기
N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
# coins.sort()

DP = [0] * (K+1)
DP[0] = 1

for i in coins:
    for j in range(i, K+1):
        DP[j] += DP[j-i]

print(DP[K])