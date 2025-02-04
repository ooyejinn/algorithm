def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(s):
        visited[s] = 1
        for i in range(n):
            if computers[s][i] == 1 and visited[i] == 0:
                dfs(i)
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i)
    
    return answer