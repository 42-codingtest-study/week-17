#
# 15051
# Máquina de café
# https://www.acmicpc.net/problem/15051

import sys
input = sys.stdin.readline

a1 = int(input())
a2 = int(input())
a3 = int(input())

p1 = a2 * 2 + a3 * 4
p2 = a1 * 2 + a3 * 2
p3 = a1 * 4 + a2 * 2

print(min(p1, p2, p3))