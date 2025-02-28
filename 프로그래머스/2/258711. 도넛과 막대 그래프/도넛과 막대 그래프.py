# 간선 방향이 있음 (중요)

# 새 정점
# S: 2 이상
# E: 0

# 막대 그래프의 경우: S: 0-1 // E: 0-2
# S0, E1  (size:1 || 마지막 노드인데 연결되지 않음)
# S1, E1 (중간 노드인데 연결되지 않음)
# S1, E2 (중간 노드인데 연결됨)
# S1, E0 (첫번째 노드인데 연결되지 않음)

# 도넛 그래프의 경우: S: 1 // E: 1-2
# S1, E2 (size:1 || size: 2 이상이며 연결됨)
# S1, E1 (size:2, 연결되지 않음)
# S1, E2 (size:2, 연결됨)

# 8자 그래프의 경우: 도넛 그래프랑 똑같으나 한 케이스만 추가됨
# S2, E2 (징검다리 노드이며, 연결되지 않음)
# S2, E3 (징검다리 노드이며, 연결됨)

# -> S가 2 이상이며, E가 0인 그래프면 무조건 정점


# 그 뒤 추가된 노드 제외하고,
# 각 노드들에 방문 체크하며
# deque로 탐색해서 어떤 그래프인지 확인하고
# deque 다 하고 다음 deque에서 방문 안한 새 노드 가게되면 또 새 그래프일 것이고... 

from collections import defaultdict, deque

def solution(edges):
    
    max_node = 0
    arr = defaultdict(list)
    start_nodes = defaultdict(int)
    end_nodes = defaultdict(int)
    add_node = 0
    all_nodes = set()
    
    for s, e in edges:
        arr[s].append(e)
        max_node = max(max_node, s, e)
        start_nodes[s] += 1
        end_nodes[e] += 1
        all_nodes.add(s)
        all_nodes.add(e)
    
    for i in range(1, max_node+1):
        if end_nodes[i] == 0:
            if start_nodes[i] >= 2:
                add_node = i
                break
                
                
    arr_no_add = defaultdict(list)
    undirected = defaultdict(list)
    nodes = all_nodes - {add_node}
    
    for s in arr:
        for e in arr[s]:
            if s == add_node:
                continue
            if e == add_node:
                continue
            
            arr_no_add[s].append(e)
            undirected[s].append(e)
            undirected[e].append(s)
            
            nodes.add(s)
            nodes.add(e)
            
    
    visited = set()
    comps = []
    
    
    for v in nodes:
        if v not in visited:
            Q = deque([v])
            visited.add(v)
            comp = set()
            
            while Q:
                c = Q.popleft()
                comp.add(c)

                for n in undirected[c]:
                    if n not in visited:
                        visited.add(n)
                        Q.append(n)

            comps.append(comp)
        
    
    donut_cnt = 0
    bar_cnt = 0
    eight_cnt = 0
    
    for comp in comps:
        V = len(comp)
        E = 0
        
        for node in comp:
            for n in arr_no_add[node]:
                if n in comp:
                    E += 1
                    
        if E == V:
            donut_cnt += 1
        elif E == V - 1:
            bar_cnt += 1
        elif E == V + 1:
            eight_cnt += 1

    
    return [add_node, donut_cnt, bar_cnt, eight_cnt]