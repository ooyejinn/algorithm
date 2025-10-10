import re

def solution(files):
    parsed_files = []
    
    for file in files:
        # file: 'img33.png55'
        # parts = ['img', '33', '.png', '55']
        parts = re.split(r'(\d+)', file)
        
        head = parts[0]
        num = int(parts[1])
        
        # 튜플로 묶어 리스트에 append
        parsed_files.append((file, head.lower(), num))
        
    # python의 sorted는 key 값이 같을 경우 원래 순서를 유지한다
    sorted_files = sorted(parsed_files, key=lambda x: (x[1], x[2]))
    
    answer = [file[0] for file in sorted_files]
    
    return answer