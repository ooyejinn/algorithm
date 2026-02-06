function solution(participant, completion) {
    const d = {};
    
    for (const name of participant) {
        d[name] = (d[name] || 0) + 1;
    }
    
    for (const name of completion) {
        d[name] -= 1;
    }
    
    for (const name in d) {
        if (d[name] > 0) {
            return name;
        }
    }
}