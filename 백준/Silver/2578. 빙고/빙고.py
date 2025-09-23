arr = [list(map(int, input().split())) for _ in range(5)]

check = []
for _ in range(5):
    check.extend(map(int, input().split()))

point = {arr[i][j]: (i, j) for i in range(5) for j in range(5)}

visited = [[False] * 5 for _ in range(5)]

def cnt_bingo():
    cnt = 0
    for i in range(5):
        if all(visited[i][j] for j in range(5)):
            cnt += 1
    for j in range(5):
        if all(visited[i][j] for i in range(5)):
            cnt += 1
    if all(visited[i][i] for i in range(5)):
        cnt += 1
    if all(visited[i][4 - i] for i in range(5)):
        cnt += 1
    return cnt

for idx, num in enumerate(check, start=1):
    r, c = point[num]
    visited[r][c] = True
    if idx >= 12:
        if cnt_bingo() >= 3:
            print(idx)
            break
