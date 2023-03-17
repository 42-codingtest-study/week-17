#
# 14924
# 폰 노이만과 파리
# https://www.acmicpc.net/problem/14924

import sys
input = sys.stdin.readline

s, t, d = map(int, input().split())

print(d // (2 * s) * t)