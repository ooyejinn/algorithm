'''
1   1   1   1   2   2   3   4   5   7   9   12
                2 = (i-3) + (i-2)
                    2 = (i-3) + (i-2)
                        3 = (i-3) + (i-2)
'''

T = int(input())
for tc in range(T):
    N = int(input())

    if N == 1:
        print(1)
    elif N == 2:
        print(1)
    elif N == 3:
        print(1)

    else:
        dp = [0] * (N+1)
        dp[1], dp[2], dp[3] = 1, 1, 1

        for i in range(4, N+1):
            dp[i] = dp[i-3] + dp[i-2]

        print(dp[N])