from collections import defaultdict

N = int(input())
levels = defaultdict(set)
problem_lv = {}

for _ in range(N):
    P, L = map(int, input().split())
    levels[L].add(P)
    problem_lv[P] = L

M = int(input())

for _ in range(M):
    act = input().split()

    if act[0] == 'recommend':
        if act[1] == '1':
            max_lv = max(levels.keys())
            print(max(levels[max_lv]))
        elif act[1] == '-1':
            min_lv = min(levels.keys())
            print(min(levels[min_lv]))

    elif act[0] == 'add':
        P, L = int(act[1]), int(act[2])
        levels[L].add(P)
        problem_lv[P] = L

    elif act[0] == 'solved':
        P = int(act[1])
        L = problem_lv.pop(P)
        levels[L].remove(P)
        if not levels[L]:
            del levels[L]