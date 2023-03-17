#
# 10768
# 특별한 날
# https://www.acmicpc.net/problem/10768

import sys
input = sys.stdin.readline

month = int(input())
day = int(input())

if month == 1:
    print("Before")
elif month > 2:
    print("After")
else:
    if day < 18:
        print("Before")
    elif day == 18:
        print("Special")
    else:
        print("After")