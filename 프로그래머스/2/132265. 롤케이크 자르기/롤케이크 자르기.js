function solution(topping) {
    let cnt = 0;
    
    const leftSet = new Set();
    const rightObj = {};
    let rightCnt = 0;
    
    for (const t of topping) {
        if (!rightObj[t]) {
            rightObj[t] = 1;
            rightCnt += 1;
        } else {
            rightObj[t] += 1;
        }
    }
    
    for (const t of topping) {
        leftSet.add(t);
        rightObj[t] -= 1;
        
        if (rightObj[t] === 0) {
            delete rightObj[t];
            rightCnt -= 1;
        }
        
        if (leftSet.size === rightCnt) {
            cnt += 1;
        }
    }
    
    return cnt;
}