function solution(s) {
    const n = s.length;
    let answer = n;
    
    for (unit_num = 1; unit_num <= Math.floor(n/2); unit_num++) {
        let result = "";
        let prev_str = s.slice(0, unit_num);
        let cnt = 1;
        
        for (i = unit_num; i <= n; i += unit_num) {
            let now_str = s.slice(i, i+unit_num);
            
            if (now_str === prev_str) {
                cnt += 1;
            } else {
                result += (cnt > 1 ? String(cnt) : "") + prev_str;
                prev_str = now_str;
                cnt = 1;
            }
        }
        
        result += (cnt > 1 ? String(cnt)  : "") + prev_str;
        
        answer = Math.min(answer, result.length);
    }
    
    return answer;
}