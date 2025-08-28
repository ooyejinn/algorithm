def solution(rows, columns, queries):
    arr = [[1 + r * columns + c for c in range(columns)] for r in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        start = arr[x1][y1]
        min_val = start
        
        # 왼쪽 열을 위로 올리기
        for x in range(x1, x2):
            # arr 업데이트
            arr[x][y1] = arr[x+1][y1]
            # 최솟값 갱신
            min_val = min(min_val, arr[x][y1])
           
        # 아래 행을 왼쪽으로 밀기
        for y in range(y1, y2):
            arr[x2][y] = arr[x2][y+1]
            min_val = min(min_val, arr[x2][y])
            
        # 오른쪽 열을 아래로 내리기
        for x in range(x2, x1, -1):
            arr[x][y2] = arr[x-1][y2]
            min_val = min(min_val, arr[x][y2])
            
        # 위쪽 행을 오른쪽으로 밀기
        for y in range(y2, y1+1, -1):
            arr[x1][y] = arr[x1][y-1]
            min_val = min(min_val, arr[x1][y])
            
        arr[x1][y1+1] = start
        
        answer.append(min_val)
            
    return answer