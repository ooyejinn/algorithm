function solution(n, computers) {
    const visited = Array(n).fill(0);
    let answer = 0;
    
    function bfs(start) {
        const queue = [];
        queue.push(start);
        visited[start] = 1
        
        while(queue.length > 0) {
            c = queue.shift();
            
            for (j = 0; j < n; j ++) {
                if (!visited[j] && computers[c][j] === 1) {
                    visited[j] = 1
                    queue.push(j)
                }
            }
        }
    }
    
    for (i = 0; i < n; i ++) {
        if (!visited[i]) {
            answer += 1;
            bfs(i)
        }
    }
    
    return answer;
}