def solution(sizes):
    # x, y 중 더 큰 값을 W로, 작은 값을 H로
    w = max(max(x, y) for x, y in sizes)
    h = max(min(x, y) for x, y in sizes)
    
    return w * h