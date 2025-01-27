import sys
input = sys.stdin.readline

def roll_dice(direction):
    global dice
    a, b, c, d, e, f = dice
    if direction == 1:  # 동
        dice = [d, b, a, f, e, c]
    elif direction == 2:  # 서
        dice = [c, b, f, a, e, d]
    elif direction == 3:  # 북
        dice = [e, a, c, d, f, b]
    else:  # 남
        dice = [b, f, c, d, a, e]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]  # 위, 북, 동, 서, 남, 아래
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

for command in commands:
    nx, ny = x + dx[command-1], y + dy[command-1]
    if 0 <= nx < n and 0 <= ny < m:
        roll_dice(command)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
        x, y = nx, ny
