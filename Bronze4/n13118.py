#
# 13118
# 뉴턴과 사과
# https://www.acmicpc.net/problem/13118

import sys
input = sys.stdin.readline

p = list(map(int, input().split()))
x, y, r = map(int, input().split())

if p.count(x) == 0:
    print(0)
else:
    print(p.index(x) + 1)