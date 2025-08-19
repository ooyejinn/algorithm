from collections import deque

T = int(input())

for _ in range(T):
    acts = str(input())
    n = int(input())
    arr = input()

    if n == 0:
        Q = deque()
    else:
        #                     [1:-1]: 양끝 (대괄호) 제거
        Q = deque(map(int, arr[1:-1].split(',')))

    # False: 정방향 (맨 앞 빼내기)
    # True: 역방향 (맨 뒤 빼내기)
    flag = False
    error = False

    for act in acts:
        if act == "R":
            flag = not flag
        else:
            if not Q:
                print("error")
                error = True
                break
            if flag:
                Q.pop()
            else:
                Q.popleft()

    if not error:
        if flag:
            Q.reverse()

        # map(str, Q): Q 안의 원소들 모두 문자열로 바꾸기
        # ",".join(...) 문자열 리스트를 ,로 이어붙임
        print("[" + ",".join(map(str, Q)) + "]")