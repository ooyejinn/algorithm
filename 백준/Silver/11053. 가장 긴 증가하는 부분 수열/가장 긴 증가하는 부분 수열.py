# PyPy3     144ms   31120KB
# Python3   104ms   109240KB

N = int(input())
arr = list(map(int, input().split()))

DP = [1] * (N+1)
# DP[i] = arr[i]를 '마지막' 으로 하는 가장 긴 증가하는 부분 수열의 '길이'

# i: 현재 보는 수
# j: 그 이전의 수들 모두 확인 (i보다 작은게 있는지)
for i in range(1, N):
    for j in range(i):
        # print(DP)
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + 1)

# 역순으로 비교하는 코드 (이것만 될줄...)
# for i in range(1, N):
#     for j in range(i-1, -1, -1):
#         if arr[i] > arr[j]:
#             DP[i] = max(DP[i], DP[j] + 1)

# print(DP)
# [1, 2, 1, 3, 2, 4, 1]

# DP 배열에서 가장 큰 값 = 가장 긴 증가하는 부분 수열
print(max(DP))