dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    Q = []

    Q.append((sr, sc))
    visit[sr][sc] = 1
    cnt = 1

    while Q:
        r, c = Q.pop(0)

        for k in range(4):
            nr, nc = dr[k]+r, dc[k]+c
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and arr[nr][nc] == 1:
                visit[nr][nc] = 1
                Q.append((nr, nc))
                cnt += 1

    return cnt

N = int(input())
arr = [list(map(int, input())) for i in range(N)]
visit = [[0]*N for _ in range(N)]
result = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visit[r][c] == 0:
            result.append(bfs(r, c))

result.sort()
print(len(result))
for l in result:
    print(l)