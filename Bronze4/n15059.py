#
# 15059
# Hard choice
# https://www.acmicpc.net/problem/15059

import sys
input = sys.stdin.readline

ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

cnt = 0

if ca < cr:
    cnt += cr - ca
if ba < br:
    cnt += br - ba
if pa < pr:
    cnt += pr - pa

print(cnt)