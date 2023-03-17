#
# 9782
# Median
# https://www.acmicpc.net/problem/9782

cnt = 1

while 1:
    num = list(map(int, input().split()))

    n = num[0]

    if n == 0:
        exit()

    print("Case", cnt, end='')
    print(":", end=' ')

    if n % 2 != 0:
        ro = (n + 1) // 2

        print('%.1f' %(num[ro]))
    else:
        ro1 = n // 2
        ro2 = n // 2 + 1

        print('%.1f' %((num[ro1] + num[ro2]) / 2))

    cnt += 1