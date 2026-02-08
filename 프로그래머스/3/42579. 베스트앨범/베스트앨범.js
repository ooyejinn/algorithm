function solution(genres, plays) {
    const answer = [];
    
    const N = plays.length;
    // JS에는 defaultdict가 없어서 일반 객체({})를 사용합니다.
    const genres_cnt = {}; 
    
    for (let i = 0; i < N; i++) {
        const g = genres[i];
        const p = plays[i];
        
        // genres_cnt[g] += p 와 동일한 로직
        // (값이 없으면 0으로 초기화 후 더하기)
        genres_cnt[g] = (genres_cnt[g] || 0) + p;
    }
    
    const song_info = [];
    
    for (let i = 0; i < N; i++) {
        const g = genres[i];
        const p = plays[i];
        
        // Python과 똑같이 [장르총재생수(음수), 곡재생수(음수), 인덱스, 장르] 순서로 넣습니다.
        song_info.push([-genres_cnt[g], -p, i, g]);
    }
    
    // JS의 sort는 기본적으로 문자열 정렬이라, 숫자 비교 함수를 직접 넣어줘야 합니다.
    // Python의 튜플 정렬(첫번째 요소 비교 -> 같으면 두번째 -> ...)을 구현한 부분입니다.
    song_info.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0]; // 장르 총 재생수 비교
        if (a[1] !== b[1]) return a[1] - b[1]; // 곡 재생수 비교
        return a[2] - b[2];                    // 인덱스 비교 (오름차순)
    });
    
    const genres_picked = {};
    
    // Python의 unpacking (for _, _, i, g in song_info)과 비슷하게 구조분해할당 사용
    for (const [_, __, i, g] of song_info) {
        if ((genres_picked[g] || 0) < 2) {
            answer.push(i);
            genres_picked[g] = (genres_picked[g] || 0) + 1;
        }
    }
    
    return answer;
}