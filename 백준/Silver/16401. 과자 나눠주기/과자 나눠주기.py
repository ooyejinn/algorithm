import sys

# 조카의 수 M과 과자의 수 N을 입력받음
M, N = map(int, sys.stdin.readline().split())

# 과자의 길이들을 리스트로 입력받음
snacks = list(map(int, sys.stdin.readline().split()))

# 이분 탐색을 위한 시작점과 끝점 설정
start = 1
end = max(snacks)

result = 0  # 결과값 초기화

# 이분 탐색 시작
while start <= end:
    mid = (start + end) // 2  # 중간값 계산
    count = sum(snack // mid for snack in snacks)  # 현재 길이로 만들 수 있는 과자 수 계산

    if count >= M:  # 조카 수 이상으로 과자를 나눌 수 있다면
        result = mid  # 결과 갱신
        start = mid + 1  # 더 긴 길이 탐색
    else:  # 조카 수보다 적게 나눌 수 있다면
        end = mid - 1  # 더 짧은 길이 탐색

# 결과 출력
print(result)
