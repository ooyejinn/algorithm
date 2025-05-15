function makeMultiset(s) {
    s = s.toLowerCase();
    const multiset = [];

    for (let i = 0; i < s.length - 1; i++) {
        const a = s[i];
        const b = s[i + 1];
        
        if (/[a-z]/.test(a) && /[a-z]/.test(b)) {
            multiset.push(a + b);
        }
    }
    
    return multiset;
}

function countMap(arr) {
    const map = new Map();
    for (const item of arr) {
        map.set(item, (map.get(item) || 0 ) + 1);
    }
    return map;
}

function getInter(mapA, mapB) {
    const inter = new Map();
    for (const [key, valA] of mapA) {
        if (mapB.has(key)) {
            const valB = mapB.get(key);
            inter.set(key, Math.min(valA, valB));
        }
    }
    return inter;
}

function getUnion(mapA, mapB) {
    const union = new Map(mapA);
    for (const [key, valB] of mapB) {
        const valA = mapA.get(key) || 0;
        union.set(key, Math.max(valA, valB));
    }
    return union;
}

function sumValues(map) {
    let total = 0;
    for (const val of map.values()) {
        total += val;
    }
    return total;
}


function solution(str1, str2) {
    const A = makeMultiset(str1);
    const B = makeMultiset(str2);
    
    const counterA = countMap(A);
    const counterB = countMap(B);
    
    const inter = getInter(counterA, counterB);
    const union = getUnion(counterA, counterB);
    
    const interCnt = sumValues(inter);
    const unionCnt = sumValues(union);
    
    if (unionCnt === 0) return 65536;
    
    return Math.floor((interCnt / unionCnt) * 65536);
}