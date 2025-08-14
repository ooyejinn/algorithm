from collections import defaultdict

N = int(input())

# L: (P1, P2 ...)
levels = defaultdict(set)
# P1: (L), P2: (L) ...
problem_l = {}
# P1: (G), P2: (G) ...
problem_g = {}
# G: (L1: (P1, P2 ...), L2: (P3, P4 ...))
g_levels = defaultdict(lambda: defaultdict(set))

max_l = 100

for _ in range(N):
    P, L, G = map(int, input().split())
    levels[L].add(P)
    problem_l[P] = L
    problem_g[P] = G
    g_levels[G][L].add(P)

M = int(input())

for _ in range(M):
    act = input().split()

    if act[0] == "add":
        P = int(act[1])
        L = int(act[2])
        G = int(act[3])

        levels[L].add(P)
        problem_l[P] = L
        problem_g[P] = G
        g_levels[G][L].add(P)

    elif act[0] == "recommend":
        G = int(act[1])
        X = int(act[2])

        if X == 1:
            # 내림차순
            for lv in range(max_l, 0, -1):
                if g_levels[G][lv]:
                    print(max(g_levels[G][lv]))
                    break

        else:
            # 오름차순
            for lv in range(1, max_l+1):
                if g_levels[G][lv]:
                    print(min(g_levels[G][lv]))
                    break

    elif act[0] == "recommend2":
        X = int(act[1])

        if X == 1:
            for lv in range(max_l, 0, -1):
                if levels[lv]:
                    print(max(levels[lv]))
                    break

        else:
            for lv in range(1, max_l+1):
                if levels[lv]:
                    print(min(levels[lv]))
                    break

    elif act[0] == "recommend3":
        X = int(act[1])
        L = int(act[2])

        if X == 1:
            flag = False
            for lv in range(L, max_l+1):
                if levels[lv]:
                    print(min((levels[lv])))
                    flag = True
                    break
            if not flag:
                print(-1)

        else:
            flag = False
            for lv in range(min(L-1, max_l), 0, -1):
                if levels[lv]:
                    print(max(levels[lv]))
                    flag = True
                    break
            if not flag:
                print(-1)

    elif act[0] == "solved":
        P = int(act[1])
        L = problem_l.pop(P, None)
        G = problem_g.pop(P, None)

        if L is not None:
            levels[L].discard(P)
        if G is not None:
            g_levels[G][L].discard(P)