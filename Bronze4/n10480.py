#
# 10480
# Oddities
# https://www.acmicpc.net/problem/10480

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())

    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")