def solution(name):
    up_down_moves = 0
    for char in name:
        up_down_moves += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
    n = len(name)
    left_right_moves = n - 1 
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        left_right_moves = min(left_right_moves, 2*i + n - next_i, i + 2*(n - next_i))

    return up_down_moves + left_right_moves