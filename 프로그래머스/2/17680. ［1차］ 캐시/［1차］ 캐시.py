from collections import deque

def solution(cacheSize, cities):
    N = len(cities)
    answer = 0
    
    if cacheSize == 0:
        return N*5
    
    Q = deque()
    
    for i in range(N):
        city = cities[i].lower()
        
        # 만약 deque에 없다면
        if city not in Q:
            answer += 5
            
            if len(Q) < cacheSize:
                Q.append(city)
            else:
                Q.popleft()
                Q.append(city)
        
        # 만약 deque에 있다면
        else:
            answer += 1
            Q.remove(city)
            Q.append(city)
            
    return answer