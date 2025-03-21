function solution(numbers, target) {
    
    function dfs(idx, total) {
        if (idx === numbers.length) {
            return total === target ? 1:0 ;
        }
        
        const plusCnt = dfs(idx+1, total+numbers[idx])
        const minusCnt = dfs(idx+1, total-numbers[idx])
        
        return plusCnt+minusCnt
    }
    
    return dfs(0,0);
}