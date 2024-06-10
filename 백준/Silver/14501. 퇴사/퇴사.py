N = int(input())
table = [[]for _ in range(N+1)]

for idx in range(1, N+1):
    time, pay = map(int, input().split())
    table[idx] = time, pay

# 최대수익 DP로 계속 저장해갈 공간
DP = [0]*(N+2)

for date in range(N, 0, -1):
    ctime, cpay = table[date][0], table[date][1]
    # 만약 날짜 초과면 ㄴㄴ
    endday = date + ctime

    if endday > N+1:
        DP[date] = DP[date+1]

    # 아닐경우,,, max값 계속 비교해서... 흠,.,,,,,
    else:
        #             하는 경우            안 하고 다음날로 넘어간 경우
        DP[date] = max(cpay + DP[endday], DP[date + 1])

# [0, 45, 45, 45, 35, 15, 0, 0, 0]
# print(DP)
print(DP[1])