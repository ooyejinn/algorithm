from collections import deque

def bfs(s):
    Q = deque()
    # s부터 각 회원까지의 거리 저장할 리스트 (각각의 최단 거리. 그중 가장 먼 값 = 이 회원의 레벨)
    # -1 = 방문 X, s = 0 (시작점, 자기자신)
    distance = [-1]*(N+1)
    Q.append(s)
    distance[s] = 0

    while Q:
        c = Q.popleft() # 현재 탐색할 회원
        for n in graph[c]: # 걔랑 연결된 회원들 탐색
            if distance[n] == -1: # 아직 방문 전이면면
                distance[n] = distance[c] + 1 # 거리+방문 갱신
                Q.append(n) # 걔도 탐색하게 큐에 삽입
    return max(distance) # s에서 가장 먼 레벨 반환


# 사람 수
N = int(input())
graph = [[0] for _ in range(N+1)]   # 무향그래프

# 입력받는 법 숙지하기
while True:
    s1, s2 = map(int, input().split())
    if s1 == -1:
        break
    graph[s1].append(s2)
    graph[s2].append(s1)

# 각 사람 별 최대 거리
scores = [0]*(N+1)
for i in range(1, N+1):
    scores[i] = bfs(i)

# 모든 회원의 레벨 중 최소값
min_score = min(scores[1:])

# enumerate 함수: 인덱스와 원소로 이루어진 튜플로 반환됨
candidates = []
for i, lvl in enumerate(scores):
    if lvl == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)