from collections import Counter

def make_multiset(s):
    s = s.lower()
    multiset = []
    
    for i in range(len(s) - 1):
        a, b = s[i], s[i+1]
        if a.isalpha() and b.isalpha():
            multiset.append(a + b)
    return multiset

def solution(str1, str2):
    # A = [fr, ra, an, nc, ce]
    A = make_multiset(str1)
    B = make_multiset(str2)
    
    # counterA = {'fr': 1, 'ra': 1, ...}
    counterA = Counter(A)
    counterB = Counter(B)
    
    # &: 교집합, 양쪽 모두에 존재할 경우 더 적은 쪽의 개수
    # inter = {'fr': 1, 'nc': 1}
    # Counter는 딕셔너리, 리스트 모두 지원하고,
    # dict 상속받은 특수 클래스라
    # &, | 연산자는 원래 리스트만 가능하지만
    # 오버라이딩해서 이것도 계산 됨
    inter = counterA & counterB
    # |: 합집합, 양쪽 모두에 존재할 경우 더 많은 쪽의 개수
    union = counterA | counterB
    
    inter_cnt = sum(inter.values())
    union_cnt = sum(union.values())
    
    if union_cnt == 0:
        return 65536
    
    return int((inter_cnt / union_cnt) * 65536)