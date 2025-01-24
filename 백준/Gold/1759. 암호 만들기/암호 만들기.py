from itertools import combinations

# 1. 겹치지 않는 소문자
# 2. 최소 한개의 a, e, i, o, u
# 3. 최소 두개의 나머지
# 4. 정순서 (역순서 불가)

L, C = map(int, input().split())
chars = sorted(input().split())

aeiou = set(['a', 'e', 'i', 'o', 'u'])

def is_valid(pswd):
    # 만약 전해진 문자열(L개씩의 조합) 중에 aeiou가 있는 경우 그의 합
    # 아래를 한번에 쓴 것과 같음
    # aeiou_cnt = 0
    # for char in pswd
    #   if char in aeiou:
    #       aeiou_cnt += 1
    # for char in pswd:문자열의 각 문자 순회
    # if char in aeiou: 모음 집합 포함되어있는지 확인
    # 1 for ...: 조건이 참일 때마다 1 생성
    # sum: 그 합
    aeiou_cnt = sum(1 for char in pswd if char in aeiou)
    other_cnt = len(pswd) - aeiou_cnt
    return aeiou_cnt >= 1 and other_cnt >= 2

# chars의 요소들 중 요소를 L개씩 모은 모든 조합
for pswd in combinations(chars, L):
    if is_valid(pswd):
        print(''.join(pswd))