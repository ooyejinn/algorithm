import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plum = [0] + [int(input().strip()) for _ in range(T)]

# T초까지 왔을 때, 각 W 번 이동한 상태에서 얻을 수 있는 최대 자두 개수
DP = [[0]*(W+1) for _ in range(T+1)]

for t in range(1, T+1):
    # 한번도 이동하지 않은 경우 [t][0]
    DP[t][0] = DP[t-1][0] + (1 if plum[t] == 1 else 0)

    # 1번 이동한 경우부터 최대 W번 이동한 경우까지 고려
    for w in range(1, W+1):
        # 이동횟수가 짝수면 1번 나무, 홀수면 2번 나무
        c_pos = 1 if (w%2 == 0) else 2

        #             이동하지 않은 경우
        #                          현재 이동한 경우 (직전에 비해 +1 되는 것)
        DP[t][w] = max(DP[t-1][w], DP[t-1][w-1]) + (1 if plum[t] == c_pos else 0)

# 최종 시간 기준, 여러 W 중 최대값
print(max(DP[T]))