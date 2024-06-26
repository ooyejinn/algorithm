import heapq

T = int(input())
for tc in range(T):
    min_heapq = []
    max_heapq = []
    # 중복삽입 체크를 위헤 dict 형태로
    nums = dict()

    K = int(input())

    for kc in range(K):
        order, num = input().split()
        num = int(num)

        if order == 'I':
            # 중복인 경우 num 키의 값을 += 1
            if num in nums:
                nums[num] += 1
                heapq.heappush(min_heapq, num)
                heapq.heappush(max_heapq, -num)
            else:
                nums[num] = 1
                heapq.heappush(min_heapq, num)
                heapq.heappush(max_heapq, -num)

        else:
            if max_heapq:
                if num == -1:
                    # 1. heapq의 최소값 꺼냄
                    # 2. nums 딕셔너리에 해당 키의 값이 0이면
                    #     이미 삭제된 값이므로 다음으로 넘김
                    while min_heapq and nums[min_heapq[0]] == 0:
                        heapq.heappop(min_heapq)
                    if min_heapq:
                        nums[min_heapq[0]] -= 1
                        # -=1을 함으로 해당 키의 값이 0이 되었다면
                        #     heapq에서 삭제
                        if nums[min_heapq[0]] == 0:
                            heapq.heappop(min_heapq)
                else:
                    while max_heapq and nums[-max_heapq[0]] == 0:
                        heapq.heappop(max_heapq)
                    if max_heapq:
                        nums[-max_heapq[0]] -= 1
                        if nums[-max_heapq[0]] == 0:
                            heapq.heappop(max_heapq)

        while min_heapq and nums[min_heapq[0]] == 0:
            heapq.heappop(min_heapq)
        while max_heapq and nums[-max_heapq[0]] == 0:
            heapq.heappop(max_heapq)

    if not min_heapq and not max_heapq:
        print('EMPTY')
    else:
        print(-max_heapq[0], min_heapq[0])