# 아직 방문하지 않은 정점이 있다면 방문표시
# (연결되어 있는 모든 정점들 방문표시)
def dfs(s):
  visited[s] = 1
  for i in arr[s]:
    if not visited[i]:
      dfs(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)
cnt = 0

# 정점연결
for _ in range(M):
  s, e = map(int, input().split())
  arr[s].append(e)
  arr[e].append(s)

# 만약 방문하지 않은 정점이라면 방문하며 +1 (간선의 개수 +1)
for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)
    cnt += 1

print(cnt)