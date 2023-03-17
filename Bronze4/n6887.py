#
# 6887
# Squares
# https://www.acmicpc.net/problem/6887

import sys
input = sys.stdin.readline

tile = int(input())

print("The largest square has side length %d." %((int)(tile ** 0.5)))