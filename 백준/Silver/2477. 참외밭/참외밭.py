K = int(input().strip())
edges = [tuple(map(int, input().split())) for _ in range(6)]

dirs = [d for d, _ in edges]
lens = [l for _, l in edges]

w_idx = max((i for i, d in enumerate(dirs) if d in (1, 2)), key=lambda i: lens[i])
h_idx = max((i for i, d in enumerate(dirs) if d in (3, 4)), key=lambda i: lens[i])

big = lens[w_idx] * lens[h_idx]
small = lens[(w_idx + 3) % 6] * lens[(h_idx + 3) % 6]

print(K * (big - small))