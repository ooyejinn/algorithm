function solution(msg) {
    const chr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let dict = {};
    for (let i = 0; i < 26; i++) {
        dict[chr[i]] = i + 1;
    }
    
    let result = [];
    let nxt_idx = 27;
    let i = 0;
    
    while (i < msg.length) {
        let word = msg[i];
        let longest = word;
        
        // word가 dict에 있고, 다음 글자를 붙일 수 있다면 반복
        while (dict[word] !== undefined && i + word.length <= msg.length) {
            longest = word;
            if (i + word.length < msg.length) {
                word += msg[i + word.length];
            } else {
                break;
            }
        }
        
        result.push(dict[longest]);
        
        if (i + longest.length < msg.length) {
            const new_word = longest + msg[i + longest.length];
            dict[new_word] = nxt_idx;
            nxt_idx++;
        }
        
        i += longest.length;
    }
    
    return result;
}