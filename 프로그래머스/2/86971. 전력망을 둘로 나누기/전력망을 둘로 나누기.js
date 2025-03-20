function solution(n, wires) {
    let answer = Infinity;
    
    // arr = [[] for _ in range(n+1)]
    const graph = Array.from({ length: n + 1}, () => []);
    
    wires.forEach(([w1, w2]) => {
        graph[w1].push(w2);
        graph[w2].push(w1);
    });
    
    function bfs(start, cut1, cut2) {
        const queue = [start];
        const visited = new Set([start]);
        
        while (queue.length > 0) {
            const current = queue.shift();
            
            for (const next of graph[current]) {
                if ((cut1 === current && cut2 === next) || (cut2 === current && cut1 === next)) {
                    continue;
                }
                
                if (!visited.has(next)) {
                    visited.add(next);
                    queue.push(next);
                }
            }
        }
        return visited.size;
    }
    
    wires.forEach(([w1, w2]) => {
        const cntSubtree = bfs(w1, w1, w2);
        const dif = Math.abs(cntSubtree - (n - cntSubtree));
        answer = Math.min(answer, dif);
    });
    
    return answer;
}