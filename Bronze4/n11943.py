#
# 11943
# 파일 옮기기
# https://www.acmicpc.net/problem/11943

import sys
input = sys.stdin.readline


a, b = map(int, input().split())
c, d = map(int, input().split())

cnt = 0

if abs(a - c) > abs(b - d):
    if a > c:
        cnt += c
        cnt += b
    else:
        cnt += a
        cnt += d
else:
    if b > d:
        cnt += d
        cnt += a
    else:
        cnt += b
        cnt += c

print(cnt)