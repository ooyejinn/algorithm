function solution(record) {
    const answer = [];
    const user_nick = {};
    
    for (let i = 0; i < record.length; i++) {
        const parts = record[i].split(" ");
        const active = parts[0];
        const uid = parts[1];
        
        if (active === "Enter" || active === "Change") {
            user_nick[uid] = parts[2];
        }
    }
    
    for (let i = 0; i < record.length; i++) {
        const parts = record[i].split(" ");
        const active = parts[0];
        const uid = parts[1];
        
        if (active === "Enter") {
            answer.push(`${user_nick[uid]}님이 들어왔습니다.`)
        } else if (active === "Leave") {
            answer.push(`${user_nick[uid]}님이 나갔습니다.`)
        }
    }
    
    return answer;
}