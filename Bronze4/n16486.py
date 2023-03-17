#
# 16486
# 운동장 한 바퀴
# https://www.acmicpc.net/problem/16486

import sys
input = sys.stdin.readline

d1 = int(input())
d2 = int(input())

print("%.6f" %(d1 * 2 + 2 * d2 * 3.141592))