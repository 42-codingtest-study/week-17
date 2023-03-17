#
# 8710
# Koszykarz
# https://www.acmicpc.net/problem/8710

import sys
input = sys.stdin.readline

k, w, m = map(int, input().split())

x = w - k

if x % m == 0:
    print(x // m)
else:
    print(x // m + 1)