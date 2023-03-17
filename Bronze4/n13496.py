# 질문
#
# 13496
# The Merchant of Venice
# https://www.acmicpc.net/problem/13496

import sys
input = sys.stdin.readline

k = int(input())

cnt = 1
for _ in range(k):

    shipnum, speed, remainday = map(int, input().split())
    ans = 0

    for _ in range(shipnum):
        distance, vi = map(int, input().split())

        if speed * remainday >= distance:
            ans += vi

    print("Data set", cnt, end='')
    print(":")
    print(ans)
    print()

    cnt += 1