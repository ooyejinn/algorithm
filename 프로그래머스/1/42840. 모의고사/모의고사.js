function solution(answers) {
    // patterns는 변하지 않을 값이므로 const
    const patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    // patterns.map(p => ...) -> p = patterns의 각 배열
    // reduce() -> 배열 순회하며 값 누적하는 함수
    // (acc, ans, i) => ...
        // acc -> 누적 점수 (0)
        // ans -> answers[i] 즉, i번째 문제의 실제 정답
        // i -> 현재 문제의 인덱스
    // (ans === p[i % p.length] ? 1 : 0) -> 정답 ans 와 수포자 답안 p[i % p.length] 가 같으면 1점 추가, 틀리면 0점 추가
    // reduce(..., 0) -> 0부터 시작해서 점수 누적
    let scores = patterns.map(p =>
        answers.reduce((acc, ans, i) => acc + (ans === p[i % p.length] ? 1 : 0), 0)                         
    )
    
    let maxScore = Math.max(...scores);
    
    return scores.map((score, i) => score === maxScore ? i + 1 : null).filter(x => x);
}