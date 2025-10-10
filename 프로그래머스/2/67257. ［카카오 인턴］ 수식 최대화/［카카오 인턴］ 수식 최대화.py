from itertools import permutations
import re

def solution(expression):
    answer = 0
    
    # 연산자 기준 숫자 분리
    numbers = [int(num) for num in re.split(r'(\D)', expression) if num.isdigit()]
    # 숫자 기준 연산자 분리
    ops = [op for op in re.split(r'(\d+)', expression) if not op.isdigit() and op]
    
    op_types = tuple(set(ops))
    
    # 모든 우선순위 조합 생성
    op_perms = list(permutations(op_types, len(op_types)))
    
    for op_perm in op_perms:
        temp_nums = numbers[:]
        temp_ops = ops[:]
        
        # 우선순위대로 연산자 하나씩 순회
        for op in op_perm:
            i = 0
            while i < len(temp_ops):
                # 지금 볼 연산자(op)와 일치할 경우 계산(temp_ops[i])
                if temp_ops[i] == op:
                    # 해당 연산자 기준 앞 + 뒤
                    if op == "*":
                        result = temp_nums[i] * temp_nums[i+1]
                    elif op == "+":
                        result = temp_nums[i] + temp_nums[i+1]
                    elif op == "-":
                        result = temp_nums[i] - temp_nums[i+1]
                    
                    # 계산 결과 앞(i) 위치에 업데이트
                    temp_nums[i] = result
                    
                    # 계산에 쓴 숫자, 연산자 제거 (숫자 앞의 건 업데이트 됨)
                    del temp_nums[i+1]
                    del temp_ops[i]
                    
                    # 리스트 변경되었으므로 인덱스 증가시키지 않고 같은 인덱스 다시 봐야함
                    continue
                
                # 현재 위치의 연산자와 우선순위 연산자 일치하지 않을 경우 다음 인덱스
                i += 1
        
        answer = max(answer, abs(temp_nums[0]))
    
    return answer