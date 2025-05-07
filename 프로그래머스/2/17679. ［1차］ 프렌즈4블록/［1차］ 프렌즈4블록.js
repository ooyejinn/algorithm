function solution(m, n, board) {
    let new_board = board.map(r => r.split(''));
    let answer = 0;
    
    while (true) {
        let bomb = Array.from({ length: m}, () => Array(n).fill(0));
        let found = 0;
        
        for (let r = 0; r < m-1; r++) {
            for (let c = 0; c < n-1; c++) {
                if (new_board[r][c] === ' ') continue;
                
                let char = new_board[r][c];
                
                if (
                    new_board[r][c+1] === char &&
                    new_board[r+1][c] === char &&
                    new_board[r+1][c+1] === char
                ) {
                    bomb[r][c] = bomb[r][c+1] = bomb[r+1][c] = bomb[r+1][c+1] = 1;
                    found = 1;
                }
            }
        }
        
        if (found === 0) break;
        
        for (let r = 0; r < m; r++) {
            for (let c = 0; c < n; c++) {
                if (bomb[r][c]) {
                    new_board[r][c] = ' ';
                    answer += 1;
                }
            }
        }
        
        for (let c = 0; c < n; c++) {
            let stack = [];
            for (let r = m-1; r >= 0; r--) {
                if (new_board[r][c] !== ' ') {
                    stack.push(new_board[r][c]);
                }
            }
            for (let r = m-1; r >= 0; r--) {
                new_board[r][c] = stack.length > 0 ? stack.shift() : ' ';
            }
        }
    }
    
    
    return answer;
}