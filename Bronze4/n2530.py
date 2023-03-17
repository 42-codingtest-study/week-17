#
# 2530
# 인공지능 시계
# https://www.acmicpc.net/problem/2530

import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
cook = int(input())

s += cook
rest = s // 60
s %= 60

m += rest
rest = m // 60
m %= 60

h += rest
h %= 24

print(h, m, s)