N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * (K+1)

for w, v in arr:
    # print(w, v)
    # K에 w를 넣을 수 있다면
    for now_w in range(K, w - 1, -1):
        # print(f'now_w: {now_w}, 갱신전 - DP[now_w]: {DP[now_w]}')
        # DP[now_w]: 현재 무게에서의 최대 가치
        # DP[now_w - w]: 현재 물건을 추가하기 전의 무게에서의 최대 가치
        # DP[now_w]를 현재 무게에서의 최대 가치와 현재 물건을 추가한 후의 가치 중 큰 값으로 갱신
        DP[now_w] = max(DP[now_w], DP[now_w - w] + v)
        # print(f'now_w: {now_w}, 갱신후 - DP[now_w]: {DP[now_w]}')

# print(DP)
print(max(DP))