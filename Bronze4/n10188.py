#
# 10188
# Quadrilateral
# https://www.acmicpc.net/problem/10188

for _ in range(int(input())):
    a, b = map(int, input().split())

    for i in range(b):
        print('X' * a)
    print()