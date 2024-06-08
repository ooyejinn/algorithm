from collections import deque

N, M = map(int, input().split())
friendlst = [[] for _ in range(N+1)]

for i in range(M):
    f1, f2 = map(int, input().split())
    friendlst[f1].append(f2)
    friendlst[f2].append(f1)

def bfs(s):
    arr = [0] * (N+1)
    Q = deque()
    Q.append(s)

    while Q:
        c = Q.popleft()

        for next in friendlst[c]:
            if arr[next] == 0:
                arr[next] = arr[c] + 1
                Q.append(next)

    return sum(arr)


min_result = float('inf')
idx_result = 0

for idx in range(1, N+1):
    kb = bfs(idx)
    if kb < min_result:
        min_result = kb
        idx_result = idx

print(idx_result)