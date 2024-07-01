from collections import deque

# 북 동 남 서 (+1 = 오른쪽, -1 = 왼쪽)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 9

L = int(input())
turns = [input().split() for _ in range(L)]
turns = [(int(X), C) for X, C in turns]

d = 1
head_r, head_c = 0, 0
tail = deque([(0, 0)])
time = 0
turn_idx = 0

def turn(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


while True:
    time += 1
    nr = head_r + dr[d]
    nc = head_c + dc[d]

    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in tail:
        if board[nr][nc] == 9:
            # 사과 있으면 사과 먹기
            # 길이는 그대로기 때문에 처리할 필요 없음
            board[nr][nc] = 0
        else:
            # 사과 없으면 맨 끝 꼬리 삭제
            tail.popleft()

        tail.append((nr, nc))
        head_r, head_c = nr, nc

        if turn_idx < L and time == turns[turn_idx][0]:
            d = turn(d, turns[turn_idx][1])
            turn_idx += 1

    else:
        break

print(time)