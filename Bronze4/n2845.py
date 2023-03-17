#
# 2845
# 파티가 끝나고 난 뒤
# https://www.acmicpc.net/problem/2845

import sys
input = sys.stdin.readline

l, p = map(int, input().split())

people = l * p

news = list(map(int, input().split()))

for i in news:
    print(i - people, end=' ')