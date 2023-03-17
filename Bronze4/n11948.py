#
# 11948
# 과목선택
# https://www.acmicpc.net/problem/11948

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

print(a + b + c + d - min(a, b, c, d) + max(e, f))