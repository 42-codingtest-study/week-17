#
# 11549
# Identifying tea
# https://www.acmicpc.net/problem/11549

import sys
input = sys.stdin.readline

t = int(input())

tea = list(map(int, input().split()))

print(tea.count(t))