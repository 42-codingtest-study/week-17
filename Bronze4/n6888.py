#
# 6888
# Terms of Office
# https://www.acmicpc.net/problem/6888

import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

print("All positions change in year", x)
for i in range(x + 1, y + 1):
    if (i - x) % 60 == 0:
        print("All positions change in year", i)