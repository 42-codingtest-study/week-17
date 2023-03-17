#
# 15025
# Judging Moose
# https://www.acmicpc.net/problem/15025

import sys
input = sys.stdin.readline

l, r = map(int, input().split())

if l == r:
    if l == r == 0:
        print("Not a moose")
    else:
        print("Even", l + r)
else:
    print("Odd", max(l, r) * 2)