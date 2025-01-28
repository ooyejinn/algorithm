import sys
input = sys.stdin.readline

# 세로 크기 N과 가로 크기 M을 입력받음
N, M = map(int, input().split())

# 종이에 쓰여 있는 수를 2차원 리스트로 입력받음
paper = [list(map(int, input().split())) for _ in range(N)]

# 방문 여부를 저장할 2차원 리스트 초기화
visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우 방향을 나타내는 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대값을 저장할 변수 초기화
max_sum = 0

# DFS 함수 정의
def dfs(x, y, depth, total):
    global max_sum
    
    # 깊이가 4에 도달하면 최대값 갱신 후 종료
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    # 상, 하, 좌, 우 방향으로 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 범위를 벗어나거나 이미 방문한 칸이면 건너뜀
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue
        
        # 방문 처리 후 DFS 재귀 호출
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, total + paper[nx][ny])
        visited[nx][ny] = False

# 'ㅗ' 모양 테트로미노를 처리하는 함수
def check_special(x, y):
    global max_sum
    
    # 'ㅗ' 모양의 4가지 경우를 확인
    for i in range(4):
        # 기본값은 현재 위치의 값
        temp = paper[x][y]
        
        # 3개의 칸을 추가로 확인
        for j in range(3):
            # 방향 인덱스 계산 (012, 123, 230, 301)
            k = (i + j) % 4
            nx, ny = x + dx[k], y + dy[k]
            
            # 범위를 벗어나면 더 이상 확인하지 않음
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                temp = 0
                break
            
            temp += paper[nx][ny]
        
        # 최대값 갱신
        max_sum = max(max_sum, temp)

# 모든 칸에 대해 DFS와 'ㅗ' 모양 확인
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False
        check_special(i, j)

# 최대값 출력
print(max_sum)
