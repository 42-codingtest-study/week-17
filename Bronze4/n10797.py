#
# 10797
# 10부제
# https://www.acmicpc.net/problem/10797

import sys
input = sys.stdin.readline

day = int(input())

car = list(map(int, input().split()))
cnt = 0

for i in car:
    if i % 10 == day:
        cnt += 1

print(cnt)