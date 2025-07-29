function solution(k, tangerine) {
    let answer = 0;
    
    const tangerine_type = {};
    
    for (const t of tangerine) {
        tangerine_type[t] = (tangerine_type[t] || 0) + 1;
    }
    
    // [[크기1, 개수1], [크기2, 개수2]]
    const sorted_tangerine_type = Object.entries(tangerine_type).sort((a, b) => b[1] - a[1]);
    
    let cnt = 0;
    
    for (const [size, c] of sorted_tangerine_type) {
        cnt += c;
        answer += 1;
        if (cnt >= k) return answer;
    }
}