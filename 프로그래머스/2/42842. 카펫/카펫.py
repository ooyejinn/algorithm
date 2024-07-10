def solution(brown, yellow):
    total = brown + yellow

    for length in range(1, total+1):
#         나누어 떨어지면
        if total % length == 0:
            width = total // length
#             양쪽 -1씩 총 -2씩 해야함
            if (width - 2) * (length - 2) == yellow:
                return [width, length]