function solution(k, dungeons) {
    let answer = 0;
    // dungeons 의 길이만큼 false 로 채워진 배열 생성
    let visited = new Array(dungeons.length).fill(false);
    
    //           현재 체력, 현재 방문 수
    function dfs(fatigue, cnt) {
        answer = Math.max(answer, cnt);
        
        // dungeons 길이만큼 반복
        for (let i = 0; i < dungeons.length; i++) {
            const [req, cost] = dungeons[i];
            // 방문 안함 && 현재체력 >= 해당 던전 요구체력
            if (!visited[i] && fatigue >= req) {
                // 방문 처리
                visited[i] = true;
                // 체력 소모 + 재귀 호출 
                dfs(fatigue - cost, cnt + 1);
                // 백트래킹 (방문 취소 후 다음 idx의 던전 확인)
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0);
    
    return answer;
}