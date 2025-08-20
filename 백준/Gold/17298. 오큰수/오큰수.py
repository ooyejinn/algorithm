N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
stack = [] # 인덱스

for i in range(N):
    # 첫 while 에선 stack 이 비어 pass, 1부터 실행
    # stack [-1]: 스택의 맨 위 (인덱스)
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)