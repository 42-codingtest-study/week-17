#
# 5596
# 시험 점수
# https://www.acmicpc.net/problem/5596

import sys
input = sys.stdin.readline

i1, m1, s1, e1 = map(int, input().split())
i2, m2, s2, e2 = map(int, input().split())

s = i1 + m1 + s1 + e1
t = i2 + m2 + s2 + e2

if s >= t:
    print(s)
else:
    print(t)