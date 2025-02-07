import sys
input = sys.stdin.readline

N = int(input())
T = [0]*N
P = [0]*N
DP = [0]*(N+1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

for date in range(N-1, -1, -1):
    if date + T[date] > N:
        DP[date] = DP[date+1]

    else:
        # 오늘 상담 안 하는 경우
        # 오늘 상담 하는 경우: 둘 중 max
        #     P[date] 오늘 상담비 +
        #     DP[date+T[date]] 그만큼 지난 날짜 이후의 DP에 적힌 값 (payment)
        DP[date] = max(DP[date+1], P[date]+DP[date+T[date]])

print(DP[0])