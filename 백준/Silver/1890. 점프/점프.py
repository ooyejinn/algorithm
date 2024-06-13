N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

visited[0][0] = 1

for r in range(N):
    for c in range(N):
        if r == N-1 and c == N-1:
            print(visited[r][c])

        p = arr[r][c]

        # 어캐 수정해야하는지 한참 고민함...
        # 현 위치에서 p만큼 우/하단으로 이동했을 때 그 범위가 N을 넘기지 않는다면
        # 그만큼 이동시킨 위치에 현재 위치에 있는 경로의 수를 더해줌
        # 그러니까 아예 방문하지 않는 부분도 모두 체크하게 되지만
        # 대신 deque를 쓸 때처럼 리스트 자체에 추가했다 빼는 과정이 사라져서
        # DP적으로 풀리며 동작 시간이 빨라짐
        if r + p < N:
            visited[r + p][c] += visited[r][c]
        if c + p < N:
            visited[r][c + p] += visited[r][c]
