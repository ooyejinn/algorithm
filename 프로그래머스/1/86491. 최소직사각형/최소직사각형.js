function solution(sizes) {
    
    let w = Math.max(...sizes.map(([x, y]) => Math.max(x, y)));
    let h = Math.max(...sizes.map(([x, y]) => Math.min(x, y)));
    
    return w * h;
}