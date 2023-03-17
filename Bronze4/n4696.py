#
# 4696
# St. Ives
# https://www.acmicpc.net/problem/4696

import sys
input = sys.stdin.readline

while 1:
    n = float(input())

    if n == 0:
        break
    print('%.2f' %(1 + n + n**2 + n**3 + n**4))