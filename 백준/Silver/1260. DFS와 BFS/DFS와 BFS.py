from collections import deque

# 정점 개수 / 간선 개수 / 시작 정점 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def bfs(s):
    Q = deque()
    Q.append(s)
    visited = [0]*(N+1)
    visited[s] = 1
    result = [s]

    while Q:
        cs = Q.popleft()

        for ns in graph[cs]:
            if visited[ns] == 0:
                visited[ns] = 1
                result.append(ns)
                Q.append(ns)

    return result

dfsvisited = [0]*(N+1)
def dfs(s):
    global dfsvisited

    dfsvisited[s] = 1
    result = [s]        # 현재 정점을 result 리스트에 추가

    for ns in graph[s]:
        if dfsvisited[ns] == 0:
            # result.append(dfs(ns))  # 현재의 result (한개) 에 이 이후 재귀의 result 들 이어붙임
            result.extend(dfs(ns))
    return result


# def dfs(s, visited=None):
#     if visited is None:
#         visited = [False] * (N+1)
#     visited[s] = True
#     result = [s]
#
#     for ns in graph[s]:
#         if not visited[ns]:
#             result += dfs(ns, visited)  # 재귀 호출을 통해 방문
#     return result


print(" ".join(map(str, dfs(V))))
print(" ".join(map(str, bfs(V))))