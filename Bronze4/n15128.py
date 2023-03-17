#
# 15128
# Congruent Numbers
# https://www.acmicpc.net/problem/15128

p1, q1, p2, q2 = map(int, input().split())
tri = p1/q1 * p2/q2 / 2

if int(tri) == tri:
    print(1)
else:
    print(0)