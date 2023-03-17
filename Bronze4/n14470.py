#
# 14470
# 전자레인지
# https://www.acmicpc.net/problem/14470

import sys
input = sys.stdin.readline

time = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= 0:
    time += abs(a) * c
    time += d
    a = 0

time += (b - a) * e

print(time)

