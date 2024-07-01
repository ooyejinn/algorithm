'''
핵심 알고리즘
모든 회의의 가치가 똑같으므로, 이 다음에 가장 일찍 "끝나는" 회의를 무조건 선택한다
그리디인듯?
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

end = 0
result = 0

for s, e in arr:
    if end <= s:
        result += 1
        end = e

print(result)