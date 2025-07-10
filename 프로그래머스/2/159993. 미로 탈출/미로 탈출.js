function solution(maps) {
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  const n = maps.length;
  const m = maps[0].length;

  function find(sr, sc) {
    const visited = Array.from({ length: n }, () => Array(m).fill(0));
    const Q = [[sr, sc, 0, 0]];        // r, c, cnt, flag
    let head = 0;

    while (head < Q.length) {
      const [cr, cc, cnt, flag] = Q[head++];

      if (flag === 0) {                 // 레버 전
        for (let d = 0; d < 4; d++) {
          const nr = cr + dr[d];
          const nc = cc + dc[d];
          if (0 <= nr && nr < n && 0 <= nc && nc < m && !visited[nr][nc]) {
            visited[nr][nc] = 1;        // 레버 전 방문 표시
            if (maps[nr][nc] === 'L') {
              Q.push([nr, nc, cnt + 1, 1]);
            } else if (['O', 'S', 'E'].includes(maps[nr][nc])) {
              Q.push([nr, nc, cnt + 1, 0]);
            }
          }
        }
      } else {                          // 레버 후
        for (let d = 0; d < 4; d++) {
          const nr = cr + dr[d];
          const nc = cc + dc[d];
          if (
            0 <= nr && nr < n && 0 <= nc && nc < m &&
            (visited[nr][nc] === 0 || visited[nr][nc] === 1)
          ) {
            visited[nr][nc] = 2;        // 레버 후 방문 표시
            if (maps[nr][nc] === 'E') return cnt + 1;
            if (maps[nr][nc] === 'S' || maps[nr][nc] === 'O') {
              Q.push([nr, nc, cnt + 1, 1]);
            }
          }
        }
      }
    }
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      if (maps[r][c] === 'S') return find(r, c) ?? -1;
    }
  }
}
