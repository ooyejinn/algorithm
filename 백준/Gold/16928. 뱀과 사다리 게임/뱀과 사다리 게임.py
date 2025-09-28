from collections import deque

def main():
    N, M = map(int, input().split())
    jump = list(range(101))
    for _ in range(N + M):
        a, b = map(int, input().split())
        jump[a] = b

    dist = [-1] * 101
    dist[1] = 0
    q = deque([1])

    while q:
        x = q.popleft()
        if x == 100:
            print(dist[x])
            return
        for d in range(1, 7):
            nx = x + d
            if nx > 100:
                continue
            nx = jump[nx]
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

    print(dist[100])

if __name__ == "__main__":
    main()
