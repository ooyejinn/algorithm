'''
둘 중 하나라도 자기보다 낮은 등수 있는 사람 있으면 채용!

핵심 알고리즘
1. doc 기준 정렬
2. doc 기준 정렬한 arr[0] 지원자는 무조건 채용 (그보다 낮은 doc 순위 없으니)
3. 이후로는 arr[0] 지원자보다 doc은 무조건 낮은 순위임 (동순위 없으므로)
4. 그러니 이후로는 itv만 체크하면 됨 (arr[i][1])
'''

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