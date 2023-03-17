#
# 16017
# Telemarketer or not?
# https://www.acmicpc.net/problem/16017

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 8 or a == 9:
    if b == c:
        if d == 8 or d == 9:
            print("ignore")
            exit()

print("answer")