dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    Q = []

    Q.append((r, c))
    visit[r][c] = 1
    cnt = 1

    while Q:
        i, j = Q.pop(0)

        for k in range(4):
            ni = dr[k] + i
            nj = dc[k] + j
            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and mp[ni][nj] == 1:
                visit[ni][nj] = 1
                Q.append((ni, nj))
                cnt += 1

    return cnt


N = int(input())
mp = [list(map(int, input())) for i in range(N)]
visit = [[0]*N for _ in range(N)]
result = []

for r in range(N):
    for c in range(N):
        if mp[r][c] == 1 and visit[r][c] == 0:
            result.append(bfs(r, c))

result.sort()
print(len(result))
for l in result:
    print(l)