from itertools import combinations
from collections import deque

# 구역의 개수
N = int(input())
# 구역의 인구 (1번부터 N번까지)
population = list(map(int, input().split()))
# 각 구역과 인접한 구역의 정보 (인접한 구역의 수 + 인접한 구역 번호)
array = [[] for _ in range(N)]

# 인접 구역 정보 input 받아서 array 에 집어넣기
for i in range(N):
    array_info = list(map(int, input().split()))
    for j in range(1, len(array_info)): # for j in range(1, array_info[0]+1): 이게 더 안 낫나
        array[i].append(array_info[j] - 1)

# 연결 확인
def bfs(group):
    start = group[0] # 출발점부터 ㄱㄱ
    Q = deque([start])
    visited = set([start])

    while Q:
        # Q에서 구역 하나 꺼내서
        v = Q.popleft()
        # 해당 구역(v)에 인접한 구역들 확인하기
        for w in array[v]:
            # 같은 그룹이며, 방문하지 않았다면
            if w in group and w not in visited:
                Q.append(w)
                visited.add(w)

    # 모든 구역 다 방문하면 ㄱㄱ
    return len(visited) == len(group)


# 두 선거구의 인구차 계산
def cal_difference(group):
    # 첫 그룹의 인구 합
    A = sum(population[i] for i in group)
    B = sum(population) - A

    return abs(A - B)


min_diff = float('inf')


for i in range(1, N//2+1):
    # 가능한 모든 조합 만들기
    for combo in combinations(range(N), i):
        A = list(combo)
        B = [j for j in range(N) if j not in A]

        if bfs(A) and bfs(B):
            diff = cal_difference(A)
            min_diff = min(min_diff, diff)


print(min_diff if min_diff != float('inf') else -1)