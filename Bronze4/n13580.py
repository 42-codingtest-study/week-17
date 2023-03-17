#
# 13580
# Andando no tempo
# https://www.acmicpc.net/problem/13580

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b or b == c or c == a:
    print('S')
elif abs(a - b) == c or abs(b - c) == a or abs(c - a) == b:
    print('S')
else:
    print('N')