#
# 8723
# Patyki
# https://www.acmicpc.net/problem/8723

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
num = [a, b, c]
num.sort()

if a == b == c:
    print(2)
elif num[2] ** 2 == num[0] ** 2 + num[1] ** 2:
    print(1)
else:
    print(0)