'''
from itertools import combinations, permutations

nums = [1,2,3,4]

permutations: 순열 (순서 상관 O)
perm = list(permutations(nums, 2))
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

combinations: 조합 (순서 상관 X)
comb = list(combinations(nums, 2))
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

1-1. 궁수는 각각 동시에 적 하나를 공격
1-2. 거리가 D 이하인 적 중 가장 가까운 적을 공격
1-3. 그런 적이 다수일 경우 가장 왼쪽의 적을 공격
1-4. 한 적이 여러 궁수에가 공격당할 수 있음
1-5. 공격당한 적은 사망
1-6. 궁수 턴 끝난 뒤 적은 한 칸 아래로 이동
1-7. 모든 적이 격자에서 제외되면 게임이 끝남
1-8. 죽인 적을 return
'''
from copy import deepcopy
from itertools import combinations

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.append([0]*M)

def attack(archer_position, board, D):
    targets = set()
    for archer in archer_position:
        min_dist = D+1
        target = None
        for r in range(N):
            for c in range(M):
                if board[r][c] == 1:
                    # 거리 측정
                    dist = abs(N-r) + abs(archer-c)
                    if dist <= D:
                        #   최소거리보다 짧기   or  최소거리와 같고    and c가 더 앞에 있다면
                        if (dist < min_dist) or (dist == min_dist and c < target[1] if target else True):
                            min_dist = dist
                            target = (r, c) # 추가 아니고 갱신!
        if target:
            targets.add(target)

    for r, c in targets:
        board[r][c] = 0

    return len(targets)

def move_enemies(board):
    board.pop() # 맨 아래 행 제거
    board.insert(0, [0] * M)

def NoC_archer(archer_position, arr, D):
    dead_enemy = 0
    board = deepcopy(arr)

    #     any = 제너레이터 표현식 결과 중 하나라도 True일 경우 True
    #                             board[:-1]: 마지막줄 빼고 보기 (궁수 있는 줄)
    while any(1 in row for row in board[:-1]):
        dead_enemy += attack(archer_position, board, D)
        move_enemies(board)

    return dead_enemy

archer_positions = list(combinations(range(M), 3))
result = 0

for archer_position in archer_positions:
    now_result = NoC_archer(archer_position, arr, D)
    if result < now_result:
        result = now_result

print(result)