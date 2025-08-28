from collections import deque
# deque.rotate(x)
# 원소들을 오른쪽을 x칸 회전함
# x > 0: 오른쪽
# x < 0: 왼쪽
# x가 길이보다 커도, 자동으로 x%len(deque) 만큼만 회전
# d = deque([0, 1, 2, 3, 4])
# d.rotate(1)
#     deque([4, 0, 1, 2, 3])

gears = [deque(map(int, list(input().strip()))) for _ in range(4)]

N = int(input())

for _ in range(N):
    gear, d = map(int, input().split())
    gear -= 1

    # 이번 명령에서 각 톱니가 어떻게 도는지를 기록
    gears_rotation = [0, 0, 0, 0]
    gears_rotation[gear] = d

    # 왼쪽으로 전파. now_gear와 now_gear-1이 맞닿는 극 확인
    # 현재의 6, -1의 2번 인덱스 체크
    now_gear = gear
    while now_gear -1 >= 0:
        if gears[now_gear][6] != gears[now_gear -1][2]:
            gears_rotation[now_gear -1] = -gears_rotation[now_gear]
            now_gear -= 1
        else:
            # 전파 끝나면 바로 끊어야 함
            break

    now_gear = gear
    while now_gear +1 <= 3:
        if gears[now_gear][2] != gears[now_gear +1][6]:
            gears_rotation[now_gear +1] = -gears_rotation[now_gear]
            now_gear += 1
        else:
            break

    # 기록해둔 회전 적용시키기
    for i in range(4):
        if gears_rotation[i] == 1:
            gears[i].rotate(1)
        elif gears_rotation[i] == -1:
            gears[i].rotate(-1)

cnt = 0
for i in range(4):
    if gears[i][0] == 1:
        cnt += 2 ** i # 거듭제곱


print(cnt)