def solution(tickets):
    N = len(tickets)
    visited = [0] * N
    tickets.sort(key = lambda x: (x[0], x[1]))
    answer = []
    
    def dfs(route):
        if len(route) == N+1:
            answer.append(route[:])
            return True
        
        last_airport = route[-1]
        
        for i in range(N):
            if visited[i] == 0 and tickets[i][0] == last_airport:
                visited[i] = 1
                route.append(tickets[i][1])
                
                # 다음 항공권 탐색 ㄱㄱ
                if dfs(route):
                    # 근데 항공권 찾아서 돌아오는 상태면 바로 반환 ㄱㄱ
                    return True
                
                # 만약 지금 하는 대로 경로가 완성되지 않으면 백트래킹
                # 루트/방문 취소
                route.pop()
                visited[i] = 0
                
    dfs(["ICN"])
    
    return answer[0]