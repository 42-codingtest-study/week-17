#
# 6810
# ISBN
# https://www.acmicpc.net/problem/6810

import sys
input = sys.stdin.readline

sum = 91

a = int(input())
b = int(input())
c = int(input())

print("The 1-3-sum is", end=' ')
print(sum + a + b * 3 + c)