prime_num = [1] * 1001
prime_num[0] = prime_num[1] = 0

# 2 ~ 1000까지의 소수 담기
for i in range(2, 1001):
   for j in range(2, i):
       if i % j == 0:
           prime_num[i] = 0
           break
# print(prime_num)

T = int(input())
for tc in range(T):
    N = int(input())

    flag = False

    for x in range(2, 1001):
        if prime_num[x] == 0:
            continue
        for y in range(x, 1001):
            if prime_num[y] == 0:
                continue
            for z in range(y, 1001):
                if prime_num[z] == 0:
                    continue
                if x + y + z == N:
                    print(f'{x} {y} {z}')
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print(0)