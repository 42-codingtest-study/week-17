#
# 16204
# 카드 뽑기
# https://www.acmicpc.net/problem/16204

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

of = m
xf = n - m

ob = k
xb = n - k

o = min(of, ob)
x = min(xf, xb)

print(o + x)