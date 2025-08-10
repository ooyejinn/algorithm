// Node.js의 파일 시스템 모듈 불러움
// BoJ에서는 stdin을 파일처럼 읽어야 해서 fs가 필요함
const fs = require("fs");

// readFileSync(0, 'utf8'): 표준 입력을 동기적으로 받아 문자열로 반환
// .trim(): 앞뒤 공백, 개행 제거
// .split("\n"): 줄 단위로 쪼개서 문자열 배열로 만듦
const input = fs.readFileSync(0, "utf8").trim().split("\n");

// idx: 현재 몇 번째 줄을 읽고 있는지 가리키는 포인터 변수
// parseInt(..., 10): 문자열을 10진수 정수로 변환
let idx = 0;
const N = parseInt(input[idx++], 10);

const levels = new Map();
const problem_lv = new Map();

// levels의 key 중 최댓값 찾기
function maxKeyOfLevels() {
  let has = false,
    ans = -Infinity;
  for (const k of levels.keys()) {
    has = true;
    if (k > ans) ans = k;
  }
  return has ? ans : undefined;
}

// levels의 key 중 최솟값 찾기
function minKeyOfLevels() {
  let has = false,
    ans = Infinity;
  for (const k of levels.keys()) {
    has = true;
    if (k < ans) ans = k;
  }
  return has ? ans : undefined;
}

// 특정 난이도의 Set<P>에서 문제번호의 최댓값 찾기
function maxOfSet(s) {
  let has = false,
    ans = -Infinity;
  for (const v of s) {
    has = true;
    if (v > ans) ans = v;
  }
  return has ? ans : undefined;
}

// 특정 난이도의 Set<P>에서 문제번호의 최솟값 찾기
function minOfSet(s) {
  let has = false,
    ans = Infinity;
  for (const v of s) {
    has = true;
    if (v < ans) ans = v;
  }
  return has ? ans : undefined;
}

for (let i = 0; i < N; i++) {
  // 한 줄씩 넘기며, Ps, Ls로 구조분해할당
  const [Ps, Ls] = input[idx++].split(" ");
  // 10진수로 변환
  const P = parseInt(Ps, 10);
  const L = parseInt(Ls, 10);
  if (!levels.has(L)) levels.set(L, new Set());
  levels.get(L).add(P);
  problem_lv.set(P, L);
}

const M = parseInt(input[idx++], 10);
// 한번에 출력할 recommend 결과 모을 []
const out = [];

for (let i = 0; i < M; i++) {
  const act = input[idx++].split(" ");

  if (act[0] === "recommend") {
    if (act[1] === "1") {
      const max_lv = maxKeyOfLevels();
      out.push(String(maxOfSet(levels.get(max_lv))));
    } else if (act[1] === "-1") {
      const min_lv = minKeyOfLevels();
      out.push(String(minOfSet(levels.get(min_lv))));
    }
  } else if (act[0] === "add") {
    const P = parseInt(act[1], 10);
    const L = parseInt(act[2], 10);
    if (!levels.has(L)) levels.set(L, new Set());
    levels.get(L).add(P);
    problem_lv.set(P, L);
  } else if (act[0] === "solved") {
    const P = parseInt(act[1], 10);
    const L = problem_lv.get(P);
    problem_lv.delete(P);
    const set = levels.get(L);
    if (set) {
      set.delete(P);
      if (set.size === 0) levels.delete(L); // 빈 set이면 키 삭제
    }
  }
}

console.log(out.join("\n"));
