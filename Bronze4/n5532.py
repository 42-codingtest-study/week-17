#
# 5532
# 방학 숙제
# https://www.acmicpc.net/problem/5532

import sys
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

kor = 0 # 국어 소요 시간
math = 0 # 수학 소요 시간

if a % c == 0:
    kor = a // c
else:
    kor = a // c + 1

if b % d == 0:
    math = b // d
else:
    math = b // d + 1

if kor > math:
    print(l - kor)
else:
    print(l - math)