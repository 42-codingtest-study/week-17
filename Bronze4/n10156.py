#
# 10156
# 과자
# https://www.acmicpc.net/problem/10156

import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())

money = k * n - m

if money <= 0:
    print(0)
else:
    print(money)