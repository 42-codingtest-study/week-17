#
# 5928
# Contest Timing
# https://www.acmicpc.net/problem/5928

import sys
input = sys.stdin.readline

d, h, m = map(int, input().split())

t1 = 11 * 24 * 60 + 11 * 60 + 11
t2 = d * 24 * 60 + h * 60 + m

t = t2 - t1

if t < 0:
    print(-1)
else:
    print(t)