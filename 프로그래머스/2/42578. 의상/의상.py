from collections import defaultdict

def solution(clothes):
    N = len(clothes)
    wardrobe = defaultdict(int)
    
    # 같은 이름 옷 없으면 그냥 count로 해도 될거같은데?
    # -> 이 이유로 숫자값만 카운트
    for clothe in clothes:
        wardrobe[clothe[1]] += 1
    
    answer = 1
    
    for kind in wardrobe:
        # 입는 경우 + 안 입는 경우 모두 체크하기 위해 +1
        answer *= (wardrobe[kind] + 1)
        
    # 모두 안 입는 경우 제외
    return answer - 1