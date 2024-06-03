def counting_max(arr):
    # 현재 배열의 최대값 (전체 최대값X)
    max_cnt = 1
    for r in range(N):
        row_cnt = 1
        col_cnt = 1
        # 2번째거부터 체크 (비교를 위해)
        for c in range(1, N):
            if arr[r][c] == arr[r][c-1]:
                row_cnt += 1
                max_cnt = max(max_cnt, row_cnt)
            else:
                row_cnt = 1

            if arr[c][r] == arr[c-1][r]:
                col_cnt += 1
                max_cnt = max(max_cnt, col_cnt)
            else:
                col_cnt = 1
    return max_cnt


def change_candy(arr):
    now_max_cnt = 0

    for r in range(N):
        for c in range(N):
            if c+1<N:
                # 교환
                arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]
                now_max_cnt = max(now_max_cnt, counting_max(arr))
                # 돌려놓기
                arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]

            if r+1<N:
                arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
                now_max_cnt = max(now_max_cnt, counting_max(arr))
                arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
    return now_max_cnt


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

print(change_candy(arr))