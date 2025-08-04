from collections import deque
# deque 의 popleft: 선입선출

def solution(cacheSize, cities):
    N = len(cities)
    answer = 0
    
    if cacheSize == 0:
        return N * 5
    
    Q = deque()
    
    for i in range(N):
        city = cities[i].lower()
        
        if city not in Q:
            answer += 5
        
            if len(Q) < cacheSize:
                Q.append(city)
            else:
                Q.popleft()
                Q.append(city)
                
        else:
            answer += 1
            Q.remove(city)
            Q.append(city)
            
    return answer