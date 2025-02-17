def solution(numbers, target):

    N = len(numbers)
    
    def dfs(idx, c_sum):
        
        # 리프 노드까지 도달했을 때
        if idx == N:
            if c_sum == target:
                return 1
            else:
                return 0
        
        # 줄기
        plus = dfs(idx + 1, c_sum + numbers[idx])
        minus = dfs(idx + 1, c_sum - numbers[idx])
        
        # 리프 노드의 반환값이 차근차근 아래로 내려옵니다
        return plus + minus
    
    return dfs(0, 0)