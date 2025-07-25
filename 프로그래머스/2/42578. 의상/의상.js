function solution(clothes) {
    const wardrobe = {};
    const N = clothes.length;
    
    for (const clothe of clothes) {
        const kind = clothe[1];
        if (wardrobe[kind]) {
            wardrobe[kind] += 1;
        } else {
            wardrobe[kind] = 1;
        }
        
    }
    
    let answer = 1;
    
    for (const kind in wardrobe) {
        answer *= (wardrobe[kind] + 1);
    }
    
    return answer -1;
    
}