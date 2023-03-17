#
# 2440
# 별 찍기 - 3
# https://www.acmicpc.net/problem/2440

import sys
input = sys.stdin.readline

n = int(input())

for i in reversed(range(1, n + 1)):
    print('*' * i)