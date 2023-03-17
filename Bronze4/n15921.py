#
# 15921
# 수찬은 마린보이야!!
# https://www.acmicpc.net/problem/15921

import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print("divide by zero")
    exit()

practice = list(map(int, input().split()))
answer = sum(practice)/n/(sum(practice)/n)

print("%.2f" %answer)