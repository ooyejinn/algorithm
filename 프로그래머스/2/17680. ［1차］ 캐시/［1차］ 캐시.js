function solution(cacheSize, cities) {
    const N = cities.length;
    let answer = 0;
    
    if (cacheSize === 0) return N * 5;
    
    const Q = [];
    
    for (let i = 0; i < N; i++) {
        const city = cities[i].toLowerCase();
        const idx = Q.indexOf(city);
        
        // 캐시에 없는 경우
        if (idx === -1) {
            answer += 5;
            
            if (Q.length < cacheSize) {
                Q.push(city);
            } else {
                // 오래된 항목(가장 앞) 제거
                Q.shift();
                Q.push(city);
            }
    
        } else {
            answer += 1;
            Q.splice(idx, 1);
            Q.push(city);
        }
    }
    
    return answer;
}