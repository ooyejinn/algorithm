from collections import deque
import sys

# 도시 개수 N, 도로 개수 M, 거리 정보 K, 출발 도시 번호 X 입력 받기
N, M, K, X = map(int, sys.stdin.readline().split())

# 각 도시에 연결된 도로 정보를 저장할 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 도로 정보 입력 받아 그래프 구성
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시까지의 거리는 0

# BFS 수행
queue = deque([X])
while queue:
    current = queue.popleft()
    
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_city in graph[current]:
        # 아직 방문하지 않은 도시라면
        if distance[next_city] == -1:
            # 최단 거리 갱신
            distance[next_city] = distance[current] + 1
            queue.append(next_city)

# 최단 거리가 K인 모든 도시를 오름차순으로 출력
result = [i for i in range(1, N + 1) if distance[i] == K]

if len(result) == 0:
    print(-1)
else:
    for city in result:
        print(city)
