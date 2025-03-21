function solution(maps) {
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];

  const N = maps.length;
  const M = maps[0].length;
  
  // Array.from() 으로 길이 N짜리 배열 생성 후,
  // 각 요소를 길이 M인 배열(0으로 초기화)로 만듦
  const visited = Array.from({ length: N }, () => Array(M).fill(0));
  
  // 자바스크립트에는 내장 deque가 없으므로, 배열로 구현
  // (행, 열, 거리)를 한 묶음으로 저장
  const queue = [];
  queue.push([0, 0, 1]);    // (0,0) 위치, 거리 = 1
  visited[0][0] = 1;     // 방문 표시

  while (queue.length > 0) {
    // queue.shift()로 맨 앞 요소를 꺼냄 = 파이썬의 popleft()
    // 꺼낸 요소를 [r, c, dist] 형태로 변수에 할당(배열 디스트럭처링)
    const [r, c, dist] = queue.shift();

    if (r === N - 1 && c === M - 1) {
      return dist;
    }

    for (let i = 0; i < 4; i++) {
      const nr = r + dr[i];
      const nc = c + dc[i];

      if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
        if (!visited[nr][nc] && maps[nr][nc] === 1) {
          visited[nr][nc] = 1;
          queue.push([nr, nc, dist + 1]);
        }
      }
    }
  }

  return -1;
}
