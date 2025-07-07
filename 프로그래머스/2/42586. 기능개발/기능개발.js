function solution(progresses, speeds) {
    const n = speeds.length;
    const successes = [];
    
    for (let i = 0; i < n; i++) {
        const progress = progresses[i];
        const speed = speeds[i];
        const day = Math.ceil((100 - progress) / speed);
        successes.push(day);
    }
    
    const answer = [];
    let fst = successes[0];
    let cnt = 1;
    
    for (let i = 1; i < n; i++) {
        if (successes[i] <= fst) {
            cnt += 1;
        } else {
            answer.push(cnt);
            fst = successes[i];
            cnt = 1;
        }
    }
    
    answer.push(cnt);
    return answer;
}