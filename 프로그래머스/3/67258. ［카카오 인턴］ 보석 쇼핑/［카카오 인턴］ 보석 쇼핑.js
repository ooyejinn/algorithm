function solution(gems) {
    // Array는 .length 로 길이
    const N = gems.length;
    // Set는 .size 로 길이
    const M = new Set(gems).size;
    
    const gem_dict = new Map();
    
    let result_s = 0;
    let result_e = N - 1;
    
    let start = 0;
    
    for (let end = 0; end < N; end++) {
        // end 포인터의 보석 이름
        const gem = gems[end];
        // map.set(key, value): 값 넣기
        // map.get(key): 값 읽기
        // -> gem 이 있다면 기존 값을 +1,
        // -> gem이 없다면 0 + 1
        gem_dict.set(gem, (gem_dict.get(gem) || 0) + 1);
        
        while (gem_dict.size === M) {
            if (end - start < result_e - result_s) {
                result_e = end;
                result_s = start;
            }
            
            const startGem = gems[start];
            gem_dict.set(startGem, gem_dict.get(startGem) - 1);
            if (gem_dict.get(startGem) === 0) {
                gem_dict.delete(startGem);
            }
            start += 1;
        }
    }
    return [result_s + 1, result_e + 1];
}