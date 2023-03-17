#
# 5717
# 상근이의 친구들
# https://www.acmicpc.net/problem/5717

import sys
input = sys.stdin.readline

while 1:
    m, f = map(int, input().split())

    if m == f == 0:
        exit()

    print(m + f)