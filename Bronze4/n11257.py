#
# 11257
# IT Passport Examination
# https://www.acmicpc.net/problem/11257

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num, a, b, c = map(int, input().split())
    sum = a + b + c

    print(num, sum, end=' ')

    if sum >= 55:
        if a >= 10.3 and b >= 7.5 and c >= 12:
            print("PASS")
        else:
            print("FAIL")
    else:
        print('FAIL')