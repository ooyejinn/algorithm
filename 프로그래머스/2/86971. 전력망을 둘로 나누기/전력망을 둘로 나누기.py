# 노드가 N개고, 간선이 N-1개이면서, 모든 노드가 연결되어 있음
# = 사이클이 없음
from collections import deque

def solution(n, wires):
    arr = [[] for _ in range(n + 1)]
    answer = float('inf')
    
    # 유용한 문법
    for v1, v2 in wires:
        arr[v1].append(v2)
        arr[v2].append(v1)
        
    def bfs(s, cut_v):
        Q = deque([s])
        visited = set([s])
        
        while Q:
            c = Q.popleft()
            
            for new in arr[c]:
                if (new, c) == cut_v or (c, new) == cut_v:
                    continue
            
                if new not in visited:
                    visited.add(new)
                    Q.append(new)
                
        return len(visited)
    
    for v1, v2 in wires:
        cnt_subtree = bfs(v1, (v1, v2))
        dif = abs(cnt_subtree - (n - cnt_subtree))
        answer = min(dif, answer)
    
    return answer