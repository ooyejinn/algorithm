from collections import deque

def bfs(visited, T, S, E, U, D):
  Q = deque([(S, 0)])
  visited[S] = 1

  while Q:
    ns, ncnt = Q.popleft()
    
    # 만약 목표층 도달하면 ncnt 리턴
    if ns == E:
      return(ncnt)

    if ((ns + U) <= T) and not visited[ns + U]:
      Q.append((ns + U, ncnt + 1))
      visited[ns + U] = 1
    
    if ((ns - D) >= 1) and not visited[ns - D]:
      Q.append((ns - D, ncnt + 1))
      visited[ns - D] = 1

  return('use the stairs')


# Total
  # Start
    # End
      # Up
        # Down
T, S, E, U, D = map(int, input().split())
visited = [0] * (T + 1)

print(bfs(visited, T, S, E, U, D))