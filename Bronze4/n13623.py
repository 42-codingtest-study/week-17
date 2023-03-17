#
# 13623
# Zero or One
# https://www.acmicpc.net/problem/13623

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b == c:
    print("*")
else:
    if a == b and a != c:
        print("C")
    elif b == c and b != a:
        print("A")
    else:
        print("B")