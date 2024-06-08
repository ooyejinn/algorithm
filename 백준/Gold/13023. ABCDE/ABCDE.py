N, M = map(int, input().split())
friendlst = [[] for _ in range(N+1)]

for _ in range(M):
    a1, a2 = map(int, input().split())
    friendlst[a1].append(a2)
    friendlst[a2].append(a1)

def dfs(now, depth):
    if depth >=4:
        return True

    visited[now] = 1

    for next in friendlst[now]:
        if visited[next] == 0:
            if dfs(next, depth+1):
                return True
    visited[now] = 0
    return False

for i in range(1, N+1):
    visited = [0] * (N+1)
    if dfs(i, 0):
        print(1)
        break

else:
    print(0)