#
# 11945
# 뜨거운 붕어빵
# https://www.acmicpc.net/problem/11945

n, m = map(int, input().split())

bread = [0] * n

for i in range(n):
    bread[i] = input()

for i in bread:
    print(i[::-1])