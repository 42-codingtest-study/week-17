#
# 13985
# Equality
# https://www.acmicpc.net/problem/13985

import sys
input = sys.stdin.readline

form = list(input().split( ))

a = int(form[0])
b = int(form[2])
c = int(form[4])

if a + b == c:
    print("YES")
else:
    print("NO")