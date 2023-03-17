#
# 14173
# Square Pasture
# https://www.acmicpc.net/problem/14173

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

x = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
y = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)

if x > y:
    print(x ** 2)
else:
    print(y ** 2)



