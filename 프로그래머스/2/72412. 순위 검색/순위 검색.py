from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    db = defaultdict(list)
    
    for i in info:
        i = i.split()
        lan, job, career, food, score = i
        
        for l in [lan, "-"]:
            for j in [job, "-"]:
                for c in [career, "-"]:
                    for f in [food, "-"]:
                        db[l+j+c+f].append(int(score))
    
    # db의 각 key를 하나씩 꺼내 보며
    # db[key]로 점수 배열 리스트를 본다
    # 점수 배열 리스트를 오름차순으로 정리한다
    for key in db: db[key].sort()
    
    for q in query:
        # key를 어차피 하나로 보기 때문에 하나하나 나눌 필요 없음
        options = q.replace("and", "").split()
        score = int(options.pop()) # 맨 마지막 부분 (점수)
        
        # options는 현재 리스트 상태이기 때문에, 문자열로 합쳐줌
        key = "".join(options)
        answer.append(len(db[key]) - bisect_left(db[key], score))
        # bisect_left(리스트, 값)
        # : 정렬된 리스트에 값을 넣을 때, 정렬 상태를 유지하면서 가장 왼쪽이 넣을 수 있는 인덱스를 찾아준다
    
    return answer