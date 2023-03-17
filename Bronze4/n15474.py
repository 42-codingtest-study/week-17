#
# 15474
# 鉛筆 (Pencils)
# https://www.acmicpc.net/problem/15474

import sys
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())

if n % a == 0:
    px = b * (n // a)
else:
    px = b * (n // a + 1)

if n % c == 0:
    py = d * (n // c)
else:
    py = d * (n // c + 1)

if px > py:
    print(py)
else:
    print(px)
