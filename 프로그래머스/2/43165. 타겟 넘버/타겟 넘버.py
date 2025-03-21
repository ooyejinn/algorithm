def solution(numbers, target):
    N = len(numbers)
    cnt = 0
    
    def dfs(idx, total):
        nonlocal cnt
        if idx == N:
            if total == target:
                cnt += 1
            return
        
        for i in range(2):
            if i == 0:
                dfs(idx+1, total + numbers[idx])
                
            if i == 1:
                dfs(idx+1, total - numbers[idx])
                
    dfs(0, 0)
    
    return cnt