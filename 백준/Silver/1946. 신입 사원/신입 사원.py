import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # doc_arr = sorted(arr, key=lambda x: (x[0], x[1]))
    # itv_arr = sorted(arr, key=lambda x: (x[1], x[0]))
    arr.sort(key=lambda x: x[0])

    cnt = 1
    itv_rank = arr[0][1]

    for i in range(1, N):
        if arr[i][1] < itv_rank:
            cnt += 1

            itv_rank = arr[i][1]

    print(cnt)