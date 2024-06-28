N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
# coins.sort()

# DP[i] = i원을 만드는 방법의 수
DP = [0] * (K+1)
DP[0] = 1

for i in coins:
    for j in range(i, K+1):
        DP[j] += DP[j-i]

print(DP[K])
