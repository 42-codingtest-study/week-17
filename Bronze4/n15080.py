#
# 15080
# Every Second Counts
# https://www.acmicpc.net/problem/15080

import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(" : "))
h2, m2, s2 = map(int, input().split(" : "))

t1 = h1 * 60 * 60 + m1 * 60 + s1
t2 = h2 * 60 * 60 + m2 * 60 + s2

if t1 > t2:
    print(t2 - t1 + 3600 * 24)
else:
    print(t2 - t1)