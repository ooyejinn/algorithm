from collections import deque

def solution(n, wires):
    answer = float('inf')
    arr = [[] for _ in range(n+1)]
    
    for w1, w2 in wires:
        arr[w1].append(w2)
        arr[w2].append(w1)
        
    def bfs(s, cut1, cut2):
        Q = deque()
        Q.append(s)
        visited = set([s])
        
        while Q:
            c = Q.popleft()
            
            for next in arr[c]:
                if (cut1 == c and cut2 == next) or (cut2 == c and cut1 == next):
                    continue
                
                if next not in visited:
                    visited.add(next)
                    Q.append(next)
                    
        return len(visited)
        
    for w1, w2 in wires:
        cnt_subtree = bfs(w1, w1, w2)
        dif = abs(cnt_subtree - (n - cnt_subtree))
        answer = min(dif, answer)
    
    return answer