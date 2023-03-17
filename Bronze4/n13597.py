#
# 13597
# Tri-du
# https://www.acmicpc.net/problem/13597

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a == b:
    print(a)
else:
    print(max(a, b))