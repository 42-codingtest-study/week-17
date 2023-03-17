#
# 8558
# Silnia
# https://www.acmicpc.net/problem/8558

n = int(input())

mul = 1
for i in range(2, n + 1):
    mul *= i

print(mul % 10)