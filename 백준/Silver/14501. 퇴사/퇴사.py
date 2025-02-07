N = int(input())
T = [0]*N
P = [0]*N
DP = [0]*(N+1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

# N-1부터 0까지
for date in range(N-1, -1, -1):
    # 그날의 상담을 했을 때 퇴사일을 넘기는 경우: 상담불가
    # -> 다음날 값 그대로 가져오기
    if date + T[date] > N:
        DP[date] = DP[date+1]
    else:
        # 상담 안하고 넘기는 경우: 현재 상담 금액을 그대로 다음 날로 넘김
        # 상담 하는 경우 : 현재 상담 금액 + 상담 후 받을 수 있는 최대 이익
        DP[date] = max(DP[date+1], P[date]+DP[date+T[date]])

# print(DP) = [45, 45, 45, 35, 15, 0, 0, 0]
print(DP[0])