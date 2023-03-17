#
# 8760
# Schronisko
# https://www.acmicpc.net/problem/8760

z = int(input())

for _ in range(z):
    w, k = map(int, input().split())

    print(w * k // 2)