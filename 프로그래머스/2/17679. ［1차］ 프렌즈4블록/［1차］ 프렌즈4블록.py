def solution(m, n, board):
    new_board = [list(r) for r in board]
    answer = 0
    
    while True:
        bomb = [[0] * n for _ in range(m)]
        found = 0

        for r in range(m - 1):
            for c in range(n - 1):
                if new_board[r][c] == ' ':
                    continue
                    
                char = new_board[r][c]
                
                if (new_board[r][c+1] == char and
                   new_board[r+1][c] == char and
                   new_board[r+1][c+1] == char):
                    bomb[r][c] = bomb[r][c+1] = bomb[r+1][c] = bomb[r+1][c+1] = 1
                    found = 1
                    
        if found == 0:
            break
            
        for r in range(m):
            for c in range(n):
                if bomb[r][c]:
                    new_board[r][c] = ' '
                    answer += 1
                    
        # 블록 아래로 내리기
        # 한 칸씩 내리는 게 아님!
        for c in range(n):
            stack = []
            # 아래에서 위로 역주행
            for r in range(m-1, -1, -1):
                if new_board[r][c] != ' ':
                    stack.append(new_board[r][c])
            # 아래에서 위로 채우기
            # stack이 있으면 하나씩 넣고, 다 뺐으면 빈 문자열
            for r in range(m-1, -1, -1):
                new_board[r][c] = stack.pop(0) if stack else ' '
    
    return answer