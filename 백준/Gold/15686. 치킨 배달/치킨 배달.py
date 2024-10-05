from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

# 고른 chicken_comb에 대한 모든 집의 치킨거리의 합
def get_chicken_distance(houses, chicken_comb):
    sum_distance = 0
    for hr, hc in houses:
        min_dist = float('inf')
        for cr, cc in chicken_comb:
            distance = abs(hr - cr) + abs(hc - cc)
            min_dist = min(min_dist, distance)
        sum_distance += min_dist
    return sum_distance

result = float('inf')
# chickens 에서 M개를 고른 모든 조합 각각
for chicken_comb in combinations(chickens, M):
    chicken_distance = get_chicken_distance(houses, chicken_comb)
    result = min(result, chicken_distance)

print(result)