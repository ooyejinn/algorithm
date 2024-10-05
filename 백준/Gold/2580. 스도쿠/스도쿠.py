import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

empty_cells = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]

def is_valid(r, c, num):
    # 가로세로
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    # 네모
    #            r을 3으로 나눈 몫 * 3 -> 네모박스의 시작 위치
    sr, sc = 3 * (r // 3), 3 * (c // 3)
    # sr + 3, sc + 3 까지의 2중 for문
    for nr in range(sr, sr + 3):
        for nc in range(sc, sc + 3):
            if board[nr][nc] == num:
                return False
    return True

def solve(index = 0):
    if index == len(empty_cells):
        for row in board:
            print(" ".join(map(str, row)))
        return True

    r, c = empty_cells[index]
    # 가능성 있는 숫자 후보군 미리 추리기
    candidates = []
    # 빈칸에 1부터 9까지 넣어보기
    for num in range(1, 10):
        # 만약 num이 해당 빈칸에 들어갈 수 있다면 "일단" 다음
        if is_valid(r, c, num):
            candidates.append(num)
            # board[r][c] = num
            # if solve(index + 1):
            #     return True
            # board[r][c] = 0
    for num in candidates:
        board[r][c] = num
        if solve(index + 1):
            return True
        board[r][c] = 0
    # num이 통과되었지만 그 이후 빈칸을 채울 때에,
    # 1-9중 아무것도 True를 반환하지 않으면 False를 반환
    # 그러면 앞으로 돌아가서 그 이후의 다른 숫자를 하나씩 넣어보게 됨 (백트래킹)
    return False

solve()