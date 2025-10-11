def solution(s):
    num_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    answer = s
    
    for i, num in enumerate(num_lst):
        answer = answer.replace(num, str(i))    
    
    return int(answer)