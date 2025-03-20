from collections import deque

def solution(n, wires):
    answer = float('inf')
    arr = [[] for _ in range(n+1)]
    
    for w1, w2 in wires:
        arr[w1].append(w2)
        arr[w2].append(w1)
        
    def bfs(wire1, wire2):
        Q = deque()
        Q.append(wire1)
        visited = set([wire1])
        
        while Q:
            c = Q.popleft()
            
            for next in arr[c]:
                if (wire1 == c and wire2 == next) or (wire2 == c and wire1 == next):
                    continue
                
                if next not in visited:
                    visited.add(next)
                    Q.append(next)
                    
        return len(visited)
        
    for w1, w2 in wires:
        cnt_subtree = bfs(w1, w2)
        dif = abs(cnt_subtree - (n - cnt_subtree))
        answer = min(dif, answer)
    
    return answer