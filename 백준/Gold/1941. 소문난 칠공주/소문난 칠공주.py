from itertools import combinations
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
arr = [list(input().strip()) for _ in range(5)]
result = 0

positions = [(r, c) for r in range(5) for c in range(5)]

def bfs(comb):
    Q = deque([comb[0]])
    visited = [[0]*5 for _ in range(5)]
    visited[comb[0][0]][comb[0][1]] = 1
    cnt = 1

    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if (nr, nc) in comb and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                cnt += 1

    return cnt == 7

def cnt_s(comb):
    return sum(1 for r, c in comb if arr[r][c] == 'S')

for comb in combinations(positions, 7):
    if bfs(comb) and cnt_s(comb) >=4 :
        result += 1

print(result)