#
# 7595
# Triangles
# https://www.acmicpc.net/problem/7595

import sys
input = sys.stdin.readline

while 1:
    size = int(input())

    if size == 0:
        exit()

    for i in range(1, size + 1):
        print("*" * i)