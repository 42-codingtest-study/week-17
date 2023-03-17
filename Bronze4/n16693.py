#
# 16693
# Pizza Deal
# https://www.acmicpc.net/problem/16693

from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

slice = p1 / a1
hall = p2 / (r1 * r1 * pi)

if slice < hall:
    print("Slice of pizza")
else:
    print("Whole pizza")