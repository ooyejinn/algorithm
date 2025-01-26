def str_bomb(str, bomb):
    stack = []
    bomb_last = bomb[-1]
    bomb_length = len(bomb)

    for char in str:
        # 우선 현재 char를 stack에 추가
        stack.append(char)
        # 만약 현재 문자가 폭발 문자열을 마지막 문자와 같다면
        # 스택의 마지막 bomb_length 개의 문자를 결합해 폭발 문자열과 완전히 일치하는지 확인
        if char == bomb_last and ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]

    # stack에 남은 문자열을 결합
    result = ''.join(stack)
    return result if result else "FRULA"

str = input().strip()
bomb = input().strip()

print (str_bomb(str, bomb))