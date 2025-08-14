from collections import defaultdict

N = int(input())

# L: (P1, P2...)
LP_graph = defaultdict(set)
# G: {L1: P1, P2..., L2: P3, P4...}
GLP_graph = defaultdict(lambda: defaultdict(set))
# P: [L, G]
P_graph = {}
# -> solved 처리에 역방향 맵이 있으면 좋다

for _ in range(N):
    P, L, G = map(int, input().split())
    LP_graph[L].add(P)
    GLP_graph[G][L].add(P)
    P_graph[P] = (L, G)

M = int(input())

for _ in range(M):
    act = input().split()

    if act[0] == "add":
        P, L, G = int(act[1]), int(act[2]), int(act[3])
        LP_graph[L].add(P)
        GLP_graph[G][L].add(P)
        P_graph[P] = (L, G)

    elif act[0] == "solved":
        P = int(act[1])

        if P in P_graph:
            L, G = P_graph[P]
            LP_graph[L].discard(P)
            GLP_graph[G][L].discard(P)
            del P_graph[P]

    elif act[0] == "recommend":
        G, X = int(act[1]), int(act[2])

        if X == 1:
            for lv in range(100, 0, -1):
                if GLP_graph[G][lv]:
                    print(max(GLP_graph[G][lv]))
                    break
        else:
            for lv in range(1, 101):
                if GLP_graph[G][lv]:
                    print(min(GLP_graph[G][lv]))
                    break

    elif act[0] == "recommend2":
        X = int(act[1])

        if X == 1:
            for lv in range(100, 0, -1):
                if LP_graph[lv]:
                    print(max(LP_graph[lv]))
                    break
        else:
            for lv in range(1, 101):
                if LP_graph[lv]:
                    print(min(LP_graph[lv]))
                    break

    elif act[0] == "recommend3":
        X, L = int(act[1]), int(act[2])
        flag = False

        if X == 1:
            for lv in range(L, 101):
                if LP_graph[lv]:
                    print(min(LP_graph[lv]))
                    flag = True
                    break
        else:
            for lv in range(L-1, 0, -1):
                if LP_graph[lv]:
                    print(max(LP_graph[lv]))
                    flag = True
                    break

        if not flag:
            print(-1)